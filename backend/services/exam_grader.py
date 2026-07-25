"""考试 AI 批改编排服务

负责：
1. 学生交卷后自动触发 AI 批改（fire-and-forget）
2. 调度 OCR 识别 + LLM 批改（复用作业侧 GradingService + ocr_service）
3. 维护 submission 状态机：submitted → ai_grading → ai_graded → graded
4. 提供批改进度查询

设计要点：
- 不重写 LLM 调用，直接复用 backend.services.grader.grading_service
- 单题失败不影响其他题，记录 ai_error 并标记 needs_review=True
- 使用独立 DB Session（SessionLocal()），不依赖请求 Session
- 模块级 _grading_tasks 字典跟踪任务，便于进度查询和取消
"""
import asyncio
import json
import logging
import os
import httpx
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from backend.core.database import SessionLocal
from backend.models.tables import ExamSubmission, Answer, Question
from backend.services.grader import grading_service
from backend.services.ocr import ocr_service

logger = logging.getLogger("exam")

# 主观题题型（fill 仅在带图片时算主观，纯文本 fill 由 auto_grade 处理）
SUBJECTIVE_TYPES = {"essay"}


# ===== 任务跟踪 =====
_grading_tasks: dict[int, asyncio.Task] = {}  # submission_id -> asyncio.Task


def trigger_ai_grading(submission_id: int):
    """异步派发 AI 批改任务（fire-and-forget）

    调用方无需 await，任务在后台运行。
    若该 submission 已有正在运行的任务，则跳过。

    自动适配两种调用上下文：
    - async 路由：复用当前事件循环，用 create_task 派发
    - 同步路由（threadpool）：在新线程中启动独立事件循环运行批改
    """
    # 若已有任务在运行，跳过
    existing = _grading_tasks.get(submission_id)
    if existing is not None and not existing.done():
        logger.warning(f"[ExamGrader] submission {submission_id} 已有批改任务在运行，跳过")
        return

    # 尝试获取正在运行的事件循环
    try:
        loop = asyncio.get_running_loop()
        # 在 async 上下文中，直接用 create_task
        task = loop.create_task(_grader_instance.grade_submission(submission_id))
        _grading_tasks[submission_id] = task

        def _cleanup(_):
            _grading_tasks.pop(submission_id, None)
        task.add_done_callback(_cleanup)

        logger.info(f"[ExamGrader] 已派发 submission {submission_id} 的 AI 批改任务 (async context)")
    except RuntimeError:
        # 无运行中的事件循环（同步路由 threadpool），在新线程中运行
        import threading

        def _run_in_thread():
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            try:
                task = new_loop.create_task(_grader_instance.grade_submission(submission_id))
                _grading_tasks[submission_id] = task

                def _cleanup(_):
                    _grading_tasks.pop(submission_id, None)
                task.add_done_callback(_cleanup)

                logger.info(f"[ExamGrader] 已派发 submission {submission_id} 的 AI 批改任务 (thread context)")
                new_loop.run_until_complete(task)
            except Exception as e:
                logger.exception(f"[ExamGrader] 线程批改任务异常: {e}")
            finally:
                new_loop.close()

        thread = threading.Thread(target=_run_in_thread, daemon=True, name=f"exam-grader-{submission_id}")
        thread.start()


def get_grading_progress(submission_id: int) -> dict:
    """查询任务运行状态"""
    task = _grading_tasks.get(submission_id)
    return {
        "running": task is not None and not task.done(),
        "task_done": task is not None and task.done(),
    }


def cancel_grading(submission_id: int) -> bool:
    """取消正在运行的批改任务"""
    task = _grading_tasks.get(submission_id)
    if task is not None and not task.done():
        task.cancel()
        logger.info(f"[ExamGrader] 已取消 submission {submission_id} 的批改任务")
        return True
    return False


# ===== 核心服务 =====
class ExamGrader:
    """考试 AI 批改编排器"""

    async def grade_submission(self, submission_id: int) -> dict:
        """对一次考试提交进行端到端 AI 批改

        流程：
        1. 状态机检查/锁定（submitted/ai_grading → ai_grading）
        2. 预加载所有题目，避免 N+1
        3. 遍历主观题 answer，逐题调用 LLM 批改
        4. 累加客观题分数（已在 submit_exam 中写入 answer.score）
        5. 状态置为 ai_graded，等待教师审核
        """
        db: Session = SessionLocal()
        try:
            submission = db.query(ExamSubmission).filter(
                ExamSubmission.id == submission_id
            ).first()
            if not submission:
                logger.error(f"[ExamGrader] submission {submission_id} 不存在")
                return {"error": "submission not found"}

            # 状态机检查
            if submission.status not in ("submitted", "ai_grading"):
                logger.warning(
                    f"[ExamGrader] submission {submission_id} status={submission.status}, 跳过"
                )
                return {"error": f"invalid status: {submission.status}"}

            submission.status = "ai_grading"
            db.commit()

            # 预加载所有题目
            questions = {q.id: q for q in submission.exam.questions}

            # 筛选主观题答案（essay 题 + fill 题带图片）
            subjective_answers = []
            for a in submission.answers:
                q = questions.get(a.question_id)
                if not q:
                    continue
                if q.type in SUBJECTIVE_TYPES:
                    subjective_answers.append(a)
                elif q.type == "fill" and self._has_images(a):
                    subjective_answers.append(a)

            total_graded = 0
            failed = 0
            ai_total_score = 0.0

            for answer in subjective_answers:
                question = questions[answer.question_id]
                try:
                    answer.ai_status = "processing"
                    db.commit()

                    result = await self._grade_one_answer(answer, question, db)

                    # 写回 AI 结果
                    answer.ai_score = result["suggested_score"]
                    answer.ai_comment = result.get("comment", "")
                    answer.ai_confidence = result.get("confidence", 0.85)
                    answer.ai_grading_json = json.dumps(
                        result.get("grading"), ensure_ascii=False
                    ) if result.get("grading") else None
                    answer.ai_rubric_json = json.dumps(
                        result.get("rubric"), ensure_ascii=False
                    ) if result.get("rubric") else None
                    answer.ai_model_key = result.get("model_key", "standard")
                    answer.ai_graded_at = datetime.now()
                    answer.ai_status = "graded"
                    answer.ai_error = None

                    # 预填 answer.score 为 AI 分（教师可后续修改）
                    answer.score = result["suggested_score"]

                    # needs_review 判定
                    answer.needs_review = self._should_review(answer, result)

                    ai_total_score += result["suggested_score"]
                    total_graded += 1
                    logger.info(
                        f"[ExamGrader] answer {answer.id} 批改完成: "
                        f"ai_score={result['suggested_score']}, confidence={result.get('confidence', 0.85)}"
                    )

                except Exception as e:
                    logger.exception(f"[ExamGrader] answer {answer.id} 批改失败")
                    answer.ai_status = "failed"
                    answer.ai_error = f"{type(e).__name__}: {e}"
                    answer.needs_review = True
                    failed += 1
                finally:
                    db.commit()

            # 累加客观题得分（已在 submit_exam 中写入 answer.score）
            objective_score = sum(
                a.score or 0 for a in submission.answers
                if questions.get(a.question_id) and
                   questions[a.question_id].type not in SUBJECTIVE_TYPES and
                   not (questions[a.question_id].type == "fill" and self._has_images(a))
            )
            submission.score = objective_score + ai_total_score
            submission.status = "ai_graded"
            db.commit()

            logger.info(
                f"[ExamGrader] submission {submission_id} 批改完成: "
                f"graded={total_graded}, failed={failed}, "
                f"ai_total={ai_total_score}, objective={objective_score}, total={submission.score}"
            )

            return {
                "submission_id": submission_id,
                "total_graded": total_graded,
                "failed": failed,
                "ai_total_score": ai_total_score,
                "objective_score": objective_score,
                "exam_total_score": submission.exam.total_score,
            }
        finally:
            db.close()

    async def _grade_one_answer(self, answer: Answer, question: Question, db: Session) -> dict:
        """单题批改

        1. 提取学生答案文本（content 或 OCR 识别 image_urls）
        2. 根据题型调用 GradingService.grade_math / grade_essay
        3. 返回 {suggested_score, comment, confidence, grading, rubric, model_key}
        """
        # 提取学生答案文本 + OCR
        student_text, ocr_confidence, ocr_engines, image_bytes = await self._get_student_answer(answer)

        # 记录 OCR 结果
        if ocr_engines:
            answer.ocr_text = student_text if not answer.content.strip() else answer.content
            answer.ocr_confidence = ocr_confidence
            answer.ocr_engines = ocr_engines

        # 调用 LLM 批改
        total_score = int(question.score) if question.score else 10
        standard_answer = question.answer or ""

        # 题型路由：essay → grade_essay，其他（fill 带图）→ grade_math
        if question.type == "essay":
            result = await grading_service.grade_essay(
                question=question.content,
                standard_answer=standard_answer,
                student_answer_ocr=student_text,
                total_score=total_score,
                confidence=ocr_confidence,
                image_bytes=image_bytes,
            )
        else:
            # fill 带图：作为数学题批改
            result = await grading_service.grade_math(
                question=question.content,
                standard_answer=standard_answer,
                student_answer_ocr=student_text,
                total_score=total_score,
                confidence=ocr_confidence,
                image_bytes=image_bytes,
            )

        return {
            "suggested_score": result.get("suggested_score", 0),
            "comment": result.get("comment", ""),
            "confidence": result.get("confidence", 0.85),
            "grading": result.get("grading"),
            "rubric": result.get("rubric"),
            "model_key": result.get("model_key", "standard"),
        }

    async def _get_student_answer(self, answer: Answer) -> tuple[str, float, str, Optional[bytes]]:
        """提取学生答案文本

        优先级：
        1. answer.content（文本输入）- 若非空直接使用
        2. image_urls（图片答案）- 调用 OCR 识别

        返回: (text, ocr_confidence, engines_used, image_bytes)
        - text: 学生答案文本
        - ocr_confidence: OCR 置信度（无 OCR 时为 0.85）
        - engines_used: 使用的 OCR 引擎（无 OCR 时为空字符串）
        - image_bytes: 第一张图片的字节数据（用于几何辅助线分析等）
        """
        # 1. 优先使用文本输入
        if answer.content and answer.content.strip():
            return answer.content.strip(), 0.85, "", None

        # 2. OCR 识别图片
        if not self._has_images(answer):
            return "", 0.0, "", None

        image_urls = json.loads(answer.image_urls) if answer.image_urls else []
        if not image_urls:
            return "", 0.0, "", None

        # 下载第一张图片并 OCR
        try:
            image_bytes = await self._download_image(image_urls[0])
            if not image_bytes:
                return "", 0.0, "", None

            ocr_result = await ocr_service.recognize(image_bytes)
            if ocr_result and ocr_result.text:
                engines = ",".join(ocr_result.engines_used) if ocr_result.engines_used else ""
                return ocr_result.text, ocr_result.confidence, engines, image_bytes
            return "", 0.0, "", None
        except Exception as e:
            logger.warning(f"[ExamGrader] OCR 识别失败 answer {answer.id}: {e}")
            return "", 0.0, "", None

    async def _download_image(self, url: str) -> Optional[bytes]:
        """下载图片，返回字节数据

        支持本地文件路径（/uploads/...）和 HTTP URL
        """
        # 本地文件
        if url.startswith("/uploads/") or url.startswith("uploads/"):
            local_path = url.lstrip("/")
            if not os.path.exists(local_path):
                # 尝试项目根目录
                local_path = os.path.join(os.getcwd(), local_path)
            if os.path.exists(local_path):
                with open(local_path, "rb") as f:
                    return f.read()
            logger.warning(f"[ExamGrader] 本地图片不存在: {url}")
            return None

        # HTTP URL
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                resp = await client.get(url)
                resp.raise_for_status()
                return resp.content
        except Exception as e:
            logger.warning(f"[ExamGrader] 下载图片失败 {url}: {e}")
            return None

    def _has_images(self, answer: Answer) -> bool:
        """检查 answer 是否有图片答案"""
        if not answer.image_urls:
            return False
        try:
            urls = json.loads(answer.image_urls)
            return bool(urls) and len(urls) > 0
        except (json.JSONDecodeError, TypeError):
            return False

    def _should_review(self, answer: Answer, result: dict) -> bool:
        """判定是否需要教师重点审核

        虽然全部主观题都需教师确认，但 needs_review=True 的答案会红色高亮，
        帮助教师优先处理低置信度/异常情况。

        触发条件：
        1. AI 置信度 < 0.7
        2. AI 分数 < 满分的 30%（明显低分）
        3. OCR 置信度 < 0.6（手写识别不准）
        4. LLM 调用失败（ai_status=failed，由调用方处理）
        """
        confidence = result.get("confidence", 0.85)
        if confidence < 0.7:
            return True

        suggested_score = result.get("suggested_score", 0)
        max_score = answer.question.score if answer.question else 10
        if max_score > 0 and suggested_score < max_score * 0.3:
            return True

        ocr_confidence = answer.ocr_confidence or 0
        if 0 < ocr_confidence < 0.6:
            return True

        return False


# 模块级单例
_grader_instance = ExamGrader()
