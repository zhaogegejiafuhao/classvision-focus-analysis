"""批量能力增强 API - 单元测试

测试覆盖 4 个新 API：
A. 多学生批量扫描批改 - POST /scan-batch/{exam_id}
B. 试卷模板预设一键生成 - POST /templates/{exam_id}/auto-generate
C. 模板区域批量更新 - PUT /templates/{exam_id}/regions/batch
D. 批量 Excel 报告导出 - GET /export/excel-batch?submission_ids=...

测试策略：
1. 纯函数测试（_compute_auto_layout_bboxes、_PRESET_LAYOUTS 等）
2. 路由函数测试（mock db + mock current_user + mock cv2/imdecode）
"""
import asyncio
import io
import sys
import zipfile
from unittest.mock import AsyncMock, MagicMock, patch

import numpy as np

# 把项目根目录加入 sys.path
sys.path.insert(0, "d:/ClassVision")


# ============ 工具函数 ============

def _make_mock_user(role: str = "teacher", uid: int = 1):
    """构造 mock current_user"""
    u = MagicMock()
    u.role = role
    u.id = uid
    return u


def _make_mock_db():
    """构造 mock db（链式 query().filter().first()/all()）"""
    db = MagicMock()
    # 默认 query().filter().first() 返回 None
    query = MagicMock()
    filter_q = MagicMock()
    filter_q.first.return_value = None
    filter_q.all.return_value = []
    query.filter.return_value = filter_q
    query.order_by.return_value = filter_q
    query.in_.return_value = filter_q  # 不实际生效，仅占位
    db.query.return_value = query
    return db


# ============ B. 试卷模板预设一键生成 ============

def test_preset_layouts_dict():
    """测试 _PRESET_LAYOUTS 字典完整性"""
    from backend.api.answer_sheet_template_routes import _PRESET_LAYOUTS

    assert "standard_5col" in _PRESET_LAYOUTS
    assert "single_col" in _PRESET_LAYOUTS
    assert len(_PRESET_LAYOUTS) == 5

    for name, (cols, desc) in _PRESET_LAYOUTS.items():
        assert isinstance(cols, int) and 1 <= cols <= 5, f"{name} 列数无效: {cols}"
        assert isinstance(desc, str) and desc, f"{name} 描述为空"
    print("[PASS] test_preset_layouts_dict")


def test_qtype_to_region_type_mapping():
    """测试题型 → region_type 映射"""
    from backend.api.answer_sheet_template_routes import _QTYPE_TO_REGION_TYPE

    assert _QTYPE_TO_REGION_TYPE["single"] == "bubble"
    assert _QTYPE_TO_REGION_TYPE["multi"] == "bubble"
    assert _QTYPE_TO_REGION_TYPE["judge"] == "bubble"
    assert _QTYPE_TO_REGION_TYPE["fill"] == "fill"
    assert _QTYPE_TO_REGION_TYPE["essay"] == "essay"
    print("[PASS] test_qtype_to_region_type_mapping")


def test_compute_auto_layout_bboxes_5col():
    """测试 5 列布局的 bbox 计算（10 题 → 2 行 × 5 列）"""
    from backend.api.answer_sheet_template_routes import _compute_auto_layout_bboxes

    # A4 300dpi: 2480×3508
    bboxes = _compute_auto_layout_bboxes(
        img_w=2480, img_h=3508, n_questions=10, cols=5,
        top_margin_ratio=0.05, bottom_margin_ratio=0.03, side_margin_ratio=0.03,
    )

    assert len(bboxes) == 10, f"应返回 10 个 bbox，实际 {len(bboxes)}"

    # 第 1 题（i=0, col=0, row=0）
    b0 = bboxes[0]
    assert b0["x"] == 74, f"第1题 x 应=2480*0.03=74，实际={b0['x']}"
    assert b0["y"] == 175, f"第1题 y 应=3508*0.05=175，实际={b0['y']}"
    assert b0["w"] > 0 and b0["h"] > 0

    # 第 6 题（i=5, col=0, row=1）应换行
    b5 = bboxes[5]
    assert b5["x"] == b0["x"], f"第6题 x 应=第1题 x（同列），实际={b5['x']}"
    assert b5["y"] > b0["y"], "第6题 y 应>第1题 y（下一行）"

    # 所有 bbox w 应相同（同列宽）
    ws = [b["w"] for b in bboxes]
    assert len(set(ws)) == 1, f"所有 w 应相同，实际={set(ws)}"
    # 所有 bbox h 应相同（同行高）
    hs = [b["h"] for b in bboxes]
    assert len(set(hs)) == 1, f"所有 h 应相同，实际={set(hs)}"

    print(f"[PASS] test_compute_auto_layout_bboxes_5col (w={ws[0]}, h={hs[0]})")


def test_compute_auto_layout_bboxes_single_col():
    """测试单列布局（5 题竖排）"""
    from backend.api.answer_sheet_template_routes import _compute_auto_layout_bboxes

    bboxes = _compute_auto_layout_bboxes(
        img_w=1000, img_h=2000, n_questions=5, cols=1,
    )
    assert len(bboxes) == 5

    # 所有 x 应相同（单列）
    xs = [b["x"] for b in bboxes]
    assert len(set(xs)) == 1, f"单列布局 x 应相同，实际={set(xs)}"

    # y 应单调递增
    ys = [b["y"] for b in bboxes]
    assert ys == sorted(ys), f"y 应单调递增，实际={ys}"

    print(f"[PASS] test_compute_auto_layout_bboxes_single_col")


def test_compute_auto_layout_bboxes_uneven():
    """测试不均匀分布：7 题 × 3 列 = 3 行（最后一行 1 题）"""
    from backend.api.answer_sheet_template_routes import _compute_auto_layout_bboxes

    bboxes = _compute_auto_layout_bboxes(
        img_w=1500, img_h=2000, n_questions=7, cols=3,
    )
    assert len(bboxes) == 7

    # 第 7 题（i=6, col=0, row=2）应在新行
    b6 = bboxes[6]
    b3 = bboxes[3]  # 第 4 题（i=3, col=0, row=1）
    b0 = bboxes[0]  # 第 1 题
    assert b6["y"] > b3["y"] > b0["y"], "y 应随行号递增"

    print("[PASS] test_compute_auto_layout_bboxes_uneven")


def test_auto_generate_template_layout_invalid():
    """B 路由：无效布局应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_template_routes import auto_generate_template

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    # mock 考试存在
    exam = MagicMock()
    exam.id = 1
    exam.teacher_id = 1
    db.query().filter().first.return_value = exam

    # 构造 mock UploadFile
    file = MagicMock()
    file.filename = "blank.png"
    file.read = AsyncMock(return_value=b"fake")

    try:
        asyncio.run(auto_generate_template(
            exam_id=1,
            blank_file=file,
            layout="invalid_layout",
            current_user=user, db=db,
        ))
        assert False, "应抛 HTTPException(400)"
    except HTTPException as e:
        assert e.status_code == 400
        assert "invalid_layout" in str(e.detail)
    print("[PASS] test_auto_generate_template_layout_invalid")


def test_auto_generate_template_permission_denied():
    """B 路由：学生角色应返回 403"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_template_routes import auto_generate_template

    user = _make_mock_user("student", 100)
    db = _make_mock_db()
    file = MagicMock()
    file.filename = "blank.png"

    try:
        asyncio.run(auto_generate_template(
            exam_id=1, blank_file=file, layout="standard_5col",
            current_user=user, db=db,
        ))
        assert False, "应抛 HTTPException(403)"
    except HTTPException as e:
        assert e.status_code == 403
    print("[PASS] test_auto_generate_template_permission_denied")


def test_auto_generate_template_margin_out_of_range():
    """B 路由：留白比例越界应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_template_routes import auto_generate_template

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    exam = MagicMock()
    exam.id = 1
    exam.teacher_id = 1
    db.query().filter().first.return_value = exam

    file = MagicMock()
    file.filename = "blank.png"
    file.read = AsyncMock(return_value=b"fake")

    try:
        asyncio.run(auto_generate_template(
            exam_id=1, blank_file=file, layout="standard_5col",
            top_margin_ratio=0.5,  # 越界
            current_user=user, db=db,
        ))
        assert False, "应抛 HTTPException(400)"
    except HTTPException as e:
        assert e.status_code == 400
        assert "margin" in str(e.detail).lower()
    print("[PASS] test_auto_generate_template_margin_out_of_range")


def test_auto_generate_template_success():
    """B 路由：正常生成模板的完整流程"""
    from backend.api.answer_sheet_template_routes import auto_generate_template

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()

    # mock 考试存在
    exam = MagicMock()
    exam.id = 1
    exam.teacher_id = 1
    exam.title = "测试考试"
    db.query().filter().first.return_value = exam

    # mock 题目列表（10 题，5 single + 3 fill + 2 essay）
    questions = []
    for i in range(10):
        q = MagicMock()
        q.id = 100 + i
        q.type = "single" if i < 5 else ("fill" if i < 8 else "essay")
        q.order = i + 1
        questions.append(q)

    # mock query().filter().order_by().all() 返回题目
    db.query().filter().order_by().all.return_value = questions
    # 但 in_() 不会被真实调用，让 filter().all() 也返回 questions 兜底
    db.query().filter().all.return_value = questions

    # 构造 mock UploadFile + 真实图片字节（避免 cv2 解码失败）
    # 用 numpy 构造 100×100 的图片，编码为 PNG
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    import cv2
    ok, img_bytes = cv2.imencode('.png', img)
    assert ok, "构造测试图片失败"

    file = MagicMock()
    file.filename = "blank.png"
    file.read = AsyncMock(return_value=img_bytes.tobytes())

    # mock paper_template_service.create_template
    with patch("backend.api.answer_sheet_template_routes.paper_template_service.create_template", return_value=42) as mock_create:
        result = asyncio.run(auto_generate_template(
            exam_id=1,
            blank_file=file,
            layout="standard_5col",
            question_ids_json=None,
            top_margin_ratio=0.05,
            bottom_margin_ratio=0.03,
            side_margin_ratio=0.03,
            current_user=user, db=db,
        ))

    assert result["template_id"] == 42
    assert result["exam_id"] == 1
    assert result["regions_count"] == 10
    assert result["layout"] == "standard_5col"
    assert result["grid"]["rows"] == 2
    assert result["grid"]["cols"] == 5
    assert result["image_size"]["width"] == 100
    assert result["image_size"]["height"] == 100
    assert len(result["regions"]) == 10

    # 验证题型映射
    assert result["regions"][0]["region_type"] == "bubble"  # single
    assert result["regions"][5]["region_type"] == "fill"    # fill
    assert result["regions"][8]["region_type"] == "essay"   # essay

    # 验证 create_template 被调用
    mock_create.assert_called_once()
    print(f"[PASS] test_auto_generate_template_success (regions={result['regions_count']})")


# ============ C. 模板区域批量更新 ============

def test_batch_update_regions_permission_denied():
    """C 路由：学生角色应返回 403"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_template_routes import batch_update_regions

    user = _make_mock_user("student", 100)
    db = _make_mock_db()

    try:
        batch_update_regions(
            exam_id=1, regions_json="[]",
            current_user=user, db=db,
        )
        assert False, "应抛 HTTPException(403)"
    except HTTPException as e:
        assert e.status_code == 403
    print("[PASS] test_batch_update_regions_permission_denied")


def test_batch_update_regions_template_not_found():
    """C 路由：模板不存在应返回 404"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_template_routes import batch_update_regions

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    db.query().filter().first.return_value = None  # 模板不存在

    try:
        batch_update_regions(
            exam_id=999, regions_json="[]",
            current_user=user, db=db,
        )
        assert False, "应抛 HTTPException(404)"
    except HTTPException as e:
        assert e.status_code == 404
    print("[PASS] test_batch_update_regions_template_not_found")


def test_batch_update_regions_invalid_json():
    """C 路由：无效 JSON 应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_template_routes import batch_update_regions

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    # 模板存在（同时作为 Exam 查询返回值，需设 teacher_id 通过权限检查）
    template = MagicMock()
    template.id = 1
    template.teacher_id = 1
    db.query().filter().first.return_value = template

    try:
        batch_update_regions(
            exam_id=1, regions_json="not a json",
            current_user=user, db=db,
        )
        assert False, "应抛 HTTPException(400)"
    except HTTPException as e:
        assert e.status_code == 400
        assert "格式错误" in str(e.detail)
    print("[PASS] test_batch_update_regions_invalid_json")


def test_batch_update_regions_missing_fields():
    """C 路由：缺字段应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_template_routes import batch_update_regions

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    template = MagicMock()
    template.id = 1
    template.teacher_id = 1
    db.query().filter().first.return_value = template

    # 缺 bbox
    bad_regions = '[{"question_id": 1, "region_type": "bubble"}]'
    try:
        batch_update_regions(
            exam_id=1, regions_json=bad_regions,
            current_user=user, db=db,
        )
        assert False, "应抛 HTTPException(400)"
    except HTTPException as e:
        assert e.status_code == 400
        assert "bbox" in str(e.detail)
    print("[PASS] test_batch_update_regions_missing_fields")


def test_batch_update_regions_invalid_region_type():
    """C 路由：无效 region_type 应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_template_routes import batch_update_regions

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    template = MagicMock()
    template.id = 1
    template.teacher_id = 1
    db.query().filter().first.return_value = template

    bad_regions = json_str([{
        "question_id": 1, "region_type": "invalid_type",
        "bbox": {"x": 0, "y": 0, "w": 100, "h": 100},
    }])
    try:
        batch_update_regions(
            exam_id=1, regions_json=bad_regions,
            current_user=user, db=db,
        )
        assert False, "应抛 HTTPException(400)"
    except HTTPException as e:
        assert e.status_code == 400
        assert "region_type" in str(e.detail)
    print("[PASS] test_batch_update_regions_invalid_region_type")


def test_batch_update_regions_insert_only():
    """C 路由：纯新增模式（无 region_id）"""
    import json as _json
    from backend.api.answer_sheet_template_routes import batch_update_regions

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    template = MagicMock()
    template.id = 1
    template.teacher_id = 1
    db.query().filter().first.return_value = template

    regions = [
        {"question_id": 1, "region_type": "bubble", "bbox": {"x": 0, "y": 0, "w": 100, "h": 50}, "order": 1},
        {"question_id": 2, "region_type": "fill", "bbox": {"x": 0, "y": 60, "w": 100, "h": 50}, "order": 2},
    ]

    result = batch_update_regions(
        exam_id=1, regions_json=_json.dumps(regions),
        delete_missing=False,
        current_user=user, db=db,
    )

    assert result["success"] is True
    assert result["inserted"] == 2
    assert result["updated"] == 0
    assert result["deleted"] == 0
    assert result["total"] == 2
    db.commit.assert_called_once()
    print("[PASS] test_batch_update_regions_insert_only")


# ============ A. 多学生批量扫描批改 ============

def test_scan_batch_permission_denied():
    """A 路由：学生角色应返回 403"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_scan_routes import scan_batch

    user = _make_mock_user("student", 100)
    db = _make_mock_db()
    files = [MagicMock()]

    try:
        asyncio.run(scan_batch(
            exam_id=1, files=files, student_ids="1",
            current_user=user, db=db,
        ))
        assert False, "应抛 HTTPException(403)"
    except HTTPException as e:
        assert e.status_code == 403
    print("[PASS] test_scan_batch_permission_denied")


def test_scan_batch_too_many_files():
    """A 路由：超过 50 个文件应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_scan_routes import scan_batch, _MAX_BATCH_FILES

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    files = [MagicMock() for _ in range(_MAX_BATCH_FILES + 1)]

    try:
        asyncio.run(scan_batch(
            exam_id=1, files=files,
            student_ids=",".join(str(i) for i in range(_MAX_BATCH_FILES + 1)),
            current_user=user, db=db,
        ))
        assert False, "应抛 HTTPException(400)"
    except HTTPException as e:
        assert e.status_code == 400
        assert "50" in str(e.detail)
    print("[PASS] test_scan_batch_too_many_files")


def test_scan_batch_count_mismatch():
    """A 路由：文件数与学生数不一致应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_scan_routes import scan_batch

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    files = [MagicMock(), MagicMock()]  # 2 个文件
    # 但只有 1 个 student_id
    try:
        asyncio.run(scan_batch(
            exam_id=1, files=files, student_ids="1",
            current_user=user, db=db,
        ))
        assert False, "应抛 HTTPException(400)"
    except HTTPException as e:
        assert e.status_code == 400
        assert "不一致" in str(e.detail)
    print("[PASS] test_scan_batch_count_mismatch")


def test_scan_batch_invalid_student_ids():
    """A 路由：student_ids 非数字应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_scan_routes import scan_batch

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    files = [MagicMock()]

    try:
        asyncio.run(scan_batch(
            exam_id=1, files=files, student_ids="abc",
            current_user=user, db=db,
        ))
        assert False, "应抛 HTTPException(400)"
    except HTTPException as e:
        assert e.status_code == 400
        assert "格式错误" in str(e.detail)
    print("[PASS] test_scan_batch_invalid_student_ids")


def test_scan_batch_exam_not_found():
    """A 路由：考试不存在应返回 404"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_scan_routes import scan_batch

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    db.query().filter().first.return_value = None  # 考试不存在
    files = [MagicMock()]

    try:
        asyncio.run(scan_batch(
            exam_id=999, files=files, student_ids="1",
            current_user=user, db=db,
        ))
        assert False, "应抛 HTTPException(404)"
    except HTTPException as e:
        assert e.status_code == 404
    print("[PASS] test_scan_batch_exam_not_found")


def test_scan_batch_partial_failure():
    """A 路由：部分学生失败不阻塞其他学生

    场景：2 个学生，第 1 个 scan_and_grade 抛异常，第 2 个成功
    """
    from backend.api.answer_sheet_scan_routes import scan_batch

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()

    # mock 考试
    exam = MagicMock()
    exam.id = 1
    exam.title = "测试考试"
    exam.teacher_id = 1
    db.query().filter().first.return_value = exam

    # mock 学生列表（filter().all() 返回 2 个学生）
    s1 = MagicMock(); s1.id = 101; s1.name = "张三"
    s2 = MagicMock(); s2.id = 102; s2.name = "李四"
    db.query().filter().all.return_value = [s1, s2]
    # in_() 不真实生效，让 filter().all() 返回学生列表

    # mock 文件（2 个 PNG）
    import cv2
    img = np.zeros((50, 50, 3), dtype=np.uint8)
    ok, img_bytes = cv2.imencode('.png', img)
    file1 = MagicMock(); file1.filename = "s1.png"; file1.read = AsyncMock(return_value=img_bytes.tobytes())
    file2 = MagicMock(); file2.filename = "s2.png"; file2.read = AsyncMock(return_value=img_bytes.tobytes())

    # mock orchestrator.scan_and_grade：第 1 次抛异常，第 2 次成功
    success_result = MagicMock()
    success_result.submission_id = 999
    success_result.total_score = 85
    success_result.max_score = 100
    success_result.question_results = []
    success_result.attribution = {}

    call_count = [0]
    async def mock_scan(**kwargs):
        call_count[0] += 1
        if call_count[0] == 1:
            raise ValueError("OCR 引擎不可用")
        return success_result

    with patch("backend.api.answer_sheet_scan_routes.answer_sheet_orchestrator.scan_and_grade", side_effect=mock_scan):
        result = asyncio.run(scan_batch(
            exam_id=1,
            files=[file1, file2],
            student_ids="101,102",
            current_user=user, db=db,
        ))

    assert result["total"] == 2
    assert result["success"] == 1
    assert result["failed"] == 1
    assert len(result["results"]) == 2

    # 第 1 个失败
    r0 = result["results"][0]
    assert r0["student_id"] == 101
    assert r0["success"] is False
    assert "OCR" in r0["error"]

    # 第 2 个成功
    r1 = result["results"][1]
    assert r1["student_id"] == 102
    assert r1["success"] is True
    assert r1["submission_id"] == 999
    assert r1["total_score"] == 85
    print("[PASS] test_scan_batch_partial_failure")


# ============ D. 批量 Excel 报告导出 ============

def test_export_excel_batch_permission_denied():
    """D 路由：学生角色应返回 403"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import export_excel_batch

    user = _make_mock_user("student", 100)
    db = _make_mock_db()

    try:
        export_excel_batch(
            submission_ids="1,2",
            current_user=user, db=db,
        )
        assert False, "应抛 HTTPException(403)"
    except HTTPException as e:
        assert e.status_code == 403
    print("[PASS] test_export_excel_batch_permission_denied")


def test_export_excel_batch_invalid_ids():
    """D 路由：submission_ids 非数字应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import export_excel_batch

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()

    try:
        export_excel_batch(
            submission_ids="abc,def",
            current_user=user, db=db,
        )
        assert False, "应抛 HTTPException(400)"
    except HTTPException as e:
        assert e.status_code == 400
    print("[PASS] test_export_excel_batch_invalid_ids")


def test_export_excel_batch_too_many():
    """D 路由：超过 100 个 submission 应返回 400"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import export_excel_batch

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()
    # 101 个 ID
    ids = ",".join(str(i) for i in range(101))

    try:
        export_excel_batch(
            submission_ids=ids,
            current_user=user, db=db,
        )
        assert False, "应抛 HTTPException(400)"
    except HTTPException as e:
        assert e.status_code == 400
        assert "100" in str(e.detail)
    print("[PASS] test_export_excel_batch_too_many")


def test_export_excel_batch_missing_submissions():
    """D 路由：submission 不存在应返回 404"""
    from fastapi import HTTPException
    from backend.api.answer_sheet_grading_routes import export_excel_batch

    user = _make_mock_user("teacher", 1)
    db = _make_mock_db()

    # mock 查询返回空列表（所有 submission 都不存在）
    db.query().filter().all.return_value = []

    try:
        export_excel_batch(
            submission_ids="999,998",
            current_user=user, db=db,
        )
        assert False, "应抛 HTTPException(404)"
    except HTTPException as e:
        assert e.status_code == 404
        assert "999" in str(e.detail) or "998" in str(e.detail)
    print("[PASS] test_export_excel_batch_missing_submissions")


# ============ 辅助 ============

def json_str(obj):
    """序列化为 JSON 字符串（兼容中文）"""
    import json as _json
    return _json.dumps(obj, ensure_ascii=False)


# ============ 主入口 ============

def main():
    print("=" * 60)
    print("批量能力增强 API - 单元测试")
    print("=" * 60)

    # B 方案
    print("\n--- B. 试卷模板预设一键生成 ---")
    test_preset_layouts_dict()
    test_qtype_to_region_type_mapping()
    test_compute_auto_layout_bboxes_5col()
    test_compute_auto_layout_bboxes_single_col()
    test_compute_auto_layout_bboxes_uneven()
    test_auto_generate_template_layout_invalid()
    test_auto_generate_template_permission_denied()
    test_auto_generate_template_margin_out_of_range()
    test_auto_generate_template_success()

    # C 方案
    print("\n--- C. 模板区域批量更新 ---")
    test_batch_update_regions_permission_denied()
    test_batch_update_regions_template_not_found()
    test_batch_update_regions_invalid_json()
    test_batch_update_regions_missing_fields()
    test_batch_update_regions_invalid_region_type()
    test_batch_update_regions_insert_only()

    # A 方案
    print("\n--- A. 多学生批量扫描批改 ---")
    test_scan_batch_permission_denied()
    test_scan_batch_too_many_files()
    test_scan_batch_count_mismatch()
    test_scan_batch_invalid_student_ids()
    test_scan_batch_exam_not_found()
    test_scan_batch_partial_failure()

    # D 方案
    print("\n--- D. 批量 Excel 报告导出 ---")
    test_export_excel_batch_permission_denied()
    test_export_excel_batch_invalid_ids()
    test_export_excel_batch_too_many()
    test_export_excel_batch_missing_submissions()

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()

