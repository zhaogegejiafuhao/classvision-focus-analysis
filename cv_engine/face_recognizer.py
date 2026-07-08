"""人脸识别特征提取器（基于 InsightFace ArcFace）"""
import json
import logging
import os
from pathlib import Path

import cv2
import numpy as np
from insightface.app import FaceAnalysis

logger = logging.getLogger(__name__)

# 模型缓存目录
MODEL_DIR = Path(__file__).parent.parent / "models" / "insightface"


class FaceRecognizer:
    """人脸识别器：提取512维特征向量，用于人脸比对"""

    _instance = None
    _app = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def app(self) -> FaceAnalysis:
        """懒加载 InsightFace 模型"""
        if self._app is None:
            # 确保模型目录存在
            MODEL_DIR.mkdir(parents=True, exist_ok=True)

            # 初始化 InsightFace（使用 buffalo_l 模型，包含人脸检测+识别）
            logger.info("正在加载 InsightFace 模型...")
            self._app = FaceAnalysis(
                name="buffalo_l",
                root=str(MODEL_DIR),
                providers=["CPUExecutionProvider"]
            )
            self._app.prepare(ctx_id=0, det_size=(640, 640))
            logger.info("InsightFace 模型加载完成")
        return self._app

    def extract_embedding(self, frame: np.ndarray) -> np.ndarray | None:
        """
        从图像中提取人脸特征向量

        Args:
            frame: BGR格式的图像帧

        Returns:
            512维特征向量，如果没有检测到人脸则返回 None
        """
        try:
            faces = self.app.get(frame)
            if len(faces) == 0:
                return None

            # 取最大的人脸（假设是主要目标）
            largest_face = max(faces, key=lambda f: (f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))

            # 返回512维特征向量
            embedding = largest_face.embedding
            return embedding
        except Exception as e:
            logger.error(f"提取人脸特征失败: {e}")
            return None

    def extract_embedding_from_bbox(self, frame: np.ndarray, bbox: list[int]) -> np.ndarray | None:
        """
        从指定区域提取人脸特征向量

        Args:
            frame: BGR格式的图像帧
            bbox: [x1, y1, x2, y2] 人脸边界框

        Returns:
            512维特征向量，如果没有检测到人脸则返回 None
        """
        try:
            x1, y1, x2, y2 = bbox
            # 扩展边界框以确保完整人脸
            h, w = frame.shape[:2]
            margin = 20
            x1 = max(0, x1 - margin)
            y1 = max(0, y1 - margin)
            x2 = min(w, x2 + margin)
            y2 = min(h, y2 + margin)

            face_region = frame[y1:y2, x1:x2]
            if face_region.size == 0:
                return None

            faces = self.app.get(face_region)
            if len(faces) == 0:
                return None

            # 返回特征向量
            return faces[0].embedding
        except Exception as e:
            logger.error(f"从指定区域提取人脸特征失败: {e}")
            return None

    def compute_similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """
        计算两个特征向量的相似度（余弦相似度）

        Args:
            embedding1: 第一个512维特征向量
            embedding2: 第二个512维特征向量

        Returns:
            相似度分数 (0-1)，越高表示越相似
        """
        # 余弦相似度
        dot = np.dot(embedding1, embedding2)
        norm1 = np.linalg.norm(embedding1)
        norm2 = np.linalg.norm(embedding2)
        similarity = dot / (norm1 * norm2)
        return float(similarity)

    def match_face(
        self,
        embedding: np.ndarray,
        registered_embeddings: list[tuple[int, str, np.ndarray]],
        threshold: float = 0.5
    ) -> tuple[int, str] | None:
        """
        在已注册人脸库中匹配

        Args:
            embedding: 待匹配的512维特征向量
            registered_embeddings: 已注册人脸列表 [(person_id, name, embedding), ...]
            threshold: 匹配阈值，默认0.5（InsightFace推荐值）

        Returns:
            (person_id, name) 如果匹配成功，否则 None
        """
        best_match = None
        best_score = 0.0

        for person_id, name, reg_emb in registered_embeddings:
            score = self.compute_similarity(embedding, reg_emb)
            if score > best_score and score >= threshold:
                best_score = score
                best_match = (person_id, name)

        return best_match


def embedding_to_json(embedding: np.ndarray) -> str:
    """将特征向量转换为JSON字符串存储"""
    return json.dumps(embedding.tolist())


def json_to_embedding(json_str: str) -> np.ndarray:
    """从JSON字符串恢复特征向量"""
    return np.array(json.loads(json_str), dtype=np.float32)


# 全局单例
recognizer = FaceRecognizer()