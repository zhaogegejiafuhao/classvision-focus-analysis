"""
归因分析核心算法（从 attribution.py 拆分）

包含 DecayPropagate 算法及共享数据结构，被 knowledge_attribution 与 writing_attribution 复用。

核心算法：DecayPropagate — 基于知识依赖DAG的方向性衰减传播
  - 后向传播：前置知识薄弱向后传播（乘法不会→除法也弱）
  - 前向聚合：子节点全弱则父节点可能教得不好（弱信号）
  - 时间衰减：近期错题权重更高（Ebbinghaus遗忘曲线）
"""
import logging
import math
from datetime import date
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger(__name__)

from backend.services.knowledge_graph import KnowledgeGraph


@dataclass
class ErrorEvent:
    """错题事件"""
    knowledge_node_id: str
    error_weight: float       # 1.0=完全错误, 0.5=部分错误
    timestamp: date           # 错误发生日期
    question_content: str = ""  # 题目内容（用于展示）
    error_cause: str = ""       # 错因标签（计算粗心|概念混淆|审题不清|辅助线缺失|逻辑跳步|知识缺失）


@dataclass
class WeaknessResult:
    """单个知识点的薄弱度结果"""
    knowledge_id: str
    knowledge_name: str
    weakness_score: float      # 归一化薄弱度 [0, 1]
    root_cause: Optional[dict] = None  # {root_node, path, propagation_type, contribution_ratio}
    error_count: int = 0
    recent_errors: list[dict] = field(default_factory=list)
    suggestion: str = ""
    error_cause_distribution: dict = field(default_factory=dict)  # 错因分布统计，如 {"计算粗心": 3, "概念混淆": 2}


@dataclass
class AnalysisReport:
    """学情分析报告"""
    student_id: str
    analysis_date: str
    radar: dict[str, float]          # 一级维度 → 归一化得分 (1-薄弱度)
    weak_points: list[WeaknessResult]
    correction_status: dict           # {total_errors, corrected, uncorrected, correction_rate}


class DecayPropagate:
    """DecayPropagate算法实现"""

    def __init__(
        self,
        kg: KnowledgeGraph,
        alpha: float = 0.6,    # 后向传播衰减因子
        beta: float = 0.3,     # 前向聚合弱传播因子
        lambda_decay: float = 0.1,  # Ebbinghaus时间衰减系数
        gamma: float = 0.4,    # 订正完成度奖励权重
    ):
        self.kg = kg
        self.alpha = alpha
        self.beta = beta
        self.lambda_decay = lambda_decay
        self.gamma = gamma

    def _time_decay(self, error_date: date, reference_date: date) -> float:
        """Ebbinghaus遗忘曲线衰减"""
        days_since = (reference_date - error_date).days
        if days_since < 0:
            days_since = 0
        return math.exp(-self.lambda_decay * days_since)

    def _backward_propagation(self, node_id: str, decayed_weights: dict[str, float]) -> float:
        """后向传播：前置知识薄弱向后传播"""
        ancestors = self.kg.get_ancestors(node_id)
        backward_score = 0.0

        for ancestor_id in ancestors:
            if ancestor_id not in decayed_weights:
                continue
            depth = self.kg.get_depth(ancestor_id, node_id)
            if depth == float("inf"):
                continue
            # 衰减传播：距离越远影响越小
            contribution = decayed_weights[ancestor_id] * (self.alpha ** depth)
            backward_score += contribution

        return backward_score

    def _forward_aggregation(self, node_id: str, raw_scores: dict[str, float]) -> float:
        """前向聚合：子节点全弱则父节点可能教得不好"""
        children = self.kg.get_children(node_id)
        if not children:
            return 0.0

        child_scores = [raw_scores.get(cid, 0.0) for cid in children]
        # 取子节点中的最大薄弱度（弱传播）
        return max(child_scores) * self.beta if child_scores else 0.0

    def analyze(
        self,
        errors: list[ErrorEvent],
        reference_date: date | None = None,
        top_k: int = 5,
        correction_records: list[dict] | None = None,
    ) -> list[WeaknessResult]:
        """
        执行DecayPropagate分析

        Args:
            errors: 错题事件列表
            reference_date: 参考日期（默认今天）
            top_k: 返回Top-K薄弱节点
            correction_records: 订正记录列表

        Returns:
            薄弱知识点列表，按薄弱度降序排列
        """
        if reference_date is None:
            reference_date = date.today()

        # Step 1: 计算每个节点的直接错误权重（含时间衰减）
        decayed_weights: dict[str, float] = {}
        error_counts: dict[str, int] = {}
        recent_errors: dict[str, list[dict]] = {}

        for error in errors:
            decay = self._time_decay(error.timestamp, reference_date)
            weighted = error.error_weight * decay

            kid = error.knowledge_node_id
            decayed_weights[kid] = decayed_weights.get(kid, 0.0) + weighted
            error_counts[kid] = error_counts.get(kid, 0) + 1

            if kid not in recent_errors:
                recent_errors[kid] = []
            recent_errors[kid].append({
                "date": error.timestamp.isoformat(),
                "question": error.question_content,
                "error_cause": error.error_cause,
            })

        # Step 1.5: 计算每个知识点的错因分布
        cause_counts: dict[str, dict[str, int]] = {}
        for error in errors:
            kid = error.knowledge_node_id
            if kid not in cause_counts:
                cause_counts[kid] = {}
            cause = error.error_cause or "未分类"
            cause_counts[kid][cause] = cause_counts[kid].get(cause, 0) + 1

        # Step 2: 对每个节点计算综合薄弱度
        raw_scores: dict[str, float] = {}
        for node_id in self.kg.get_all_nodes():
            direct = decayed_weights.get(node_id, 0.0)
            backward = self._backward_propagation(node_id, decayed_weights)
            forward = self._forward_aggregation(node_id, raw_scores if raw_scores else {})

            # 先用 direct + backward 计算，forward在第二轮更新
            raw_scores[node_id] = direct + backward

        # Step 3: 加入前向聚合（需要第二轮计算，因为forward依赖子节点的raw_scores）
        for node_id in list(raw_scores.keys()):
            forward = self._forward_aggregation(node_id, raw_scores)
            raw_scores[node_id] = raw_scores[node_id] + forward

        # Step 3.5: 订正完成度奖励（γ × correction_bonus）
        correction_bonus = {}
        if correction_records:
            for record in correction_records:
                kid = record["knowledge_node_id"]
                corrected = record.get("corrected", False)
                correction_score = record.get("correction_score", 0.0)

                if corrected:
                    # 订正满分→薄弱度快速下降（×0.3）
                    bonus = self.gamma * correction_score
                else:
                    # 长期不订正→薄弱度持续上浮（×1.2/周，简化为固定惩罚）
                    days_since = (reference_date - record.get("timestamp", reference_date)).days if record.get("timestamp") else 7
                    penalty = self.gamma * 0.05 * min(days_since / 7, 4)  # 最多4周累积
                    bonus = -penalty

                correction_bonus[kid] = correction_bonus.get(kid, 0.0) + bonus

        # Apply correction bonus to raw_scores
        for node_id in raw_scores:
            raw_scores[node_id] = max(0, raw_scores[node_id] - correction_bonus.get(node_id, 0.0))

        # Step 4: 归一化到 [0, 1]
        max_score = max(raw_scores.values()) if raw_scores else 1.0
        if max_score == 0:
            max_score = 1.0

        normalized = {nid: score / max_score for nid, score in raw_scores.items()}

        # Step 5: 找出薄弱节点（有错误记录的 + 受传播影响的）
        results = []
        for node_id, weakness in normalized.items():
            if weakness < 0.01:  # 忽略极小值
                continue

            node = self.kg.get_node(node_id)
            if not node:
                continue

            # 找薄弱根源
            root_cause = self._find_root_cause(node_id, decayed_weights, normalized)

            result = WeaknessResult(
                knowledge_id=node_id,
                knowledge_name=node["name"],
                weakness_score=round(weakness, 4),
                root_cause=root_cause,
                error_count=error_counts.get(node_id, 0),
                recent_errors=recent_errors.get(node_id, [])[:3],  # 最多展示3条
                suggestion=self._generate_suggestion(node_id, root_cause, node["name"], cause_counts.get(node_id, {})),
                error_cause_distribution=cause_counts.get(node_id, {}),
            )
            results.append(result)

        # 按薄弱度降序排列，取Top-K
        results.sort(key=lambda r: r.weakness_score, reverse=True)
        return results[:top_k]

    def _find_root_cause(
        self,
        node_id: str,
        decayed_weights: dict[str, float],
        normalized: dict[str, float],
    ) -> Optional[dict]:
        """找出薄弱根源节点和传播路径"""
        ancestors = self.kg.get_ancestors(node_id)
        if not ancestors:
            return None

        # 找祖先中权重最大的节点作为根源
        best_ancestor = None
        best_weight = 0.0

        for ancestor_id in ancestors:
            weight = decayed_weights.get(ancestor_id, 0.0)
            if weight > best_weight:
                best_weight = weight
                best_ancestor = ancestor_id

        if best_ancestor is None or best_ancestor == node_id:
            return None

        # 构建传播路径
        path = self._build_path(best_ancestor, node_id)

        # 计算根源贡献占比
        total_weakness = normalized.get(node_id, 0.0)
        root_weakness = normalized.get(best_ancestor, 0.0)
        contribution_ratio = round(root_weakness / total_weakness, 2) if total_weakness > 0 else 0.0

        root_node = self.kg.get_node(best_ancestor)
        return {
            "root_node": best_ancestor,
            "root_name": root_node["name"] if root_node else best_ancestor,
            "path": path,
            "propagation_type": "backward",
            "contribution_ratio": contribution_ratio,
        }

    def _build_path(self, from_id: str, to_id: str) -> list[str]:
        """构建从根源到当前节点的传播路径"""
        path = [from_id]
        current = from_id

        # 简化路径构建：通过prerequisites和parent关系
        visited = {from_id}
        max_depth = 10

        while current != to_id and len(path) < max_depth:
            node = self.kg.get_node(current)
            if not node:
                break

            # 优先查找prerequisites中指向to_id方向的节点
            children = self.kg.get_children(current)
            next_node = None

            for child_id in children:
                if child_id == to_id:
                    next_node = child_id
                    break
                # 检查child的子树是否包含to_id
                if self._is_ancestor_of(child_id, to_id) and child_id not in visited:
                    next_node = child_id
                    break

            # 也检查prerequisites指向的节点
            if next_node is None:
                target_node = self.kg.get_node(to_id)
                if target_node:
                    for prereq_id in target_node.get("prerequisites", []):
                        if prereq_id == current or self._is_ancestor_of(prereq_id, current):
                            # 找到路径中需要经过的中间节点
                            pass

            if next_node is None:
                # 直接跳到目标
                break

            path.append(next_node)
            visited.add(next_node)
            current = next_node

        if current != to_id and to_id not in path:
            path.append(to_id)

        # 将ID转为名称
        return [
            self.kg.get_node(nid)["name"] if self.kg.get_node(nid) else nid
            for nid in path
        ]

    def _is_ancestor_of(self, ancestor_id: str, descendant_id: str) -> bool:
        """检查ancestor_id是否是descendant_id的祖先"""
        descendants = self.kg.get_ancestors(descendant_id)
        return ancestor_id in descendants

    @staticmethod
    def _generate_suggestion(node_id: str, root_cause: Optional[dict], node_name: str, error_cause_distribution: dict = None) -> str:
        """生成改进建议"""
        if error_cause_distribution:
            top_cause = max(error_cause_distribution, key=error_cause_distribution.get)
            total_errors = sum(error_cause_distribution.values())
            top_ratio = error_cause_distribution[top_cause] / total_errors if total_errors > 0 else 0
            if top_ratio > 0.5:
                cause_advice = {
                    "计算粗心": f"建议进行计算专项训练，提高运算准确性",
                    "概念混淆": f"建议重新理解{node_name}的核心概念，梳理易混淆点",
                    "审题不清": f"建议培养审题习惯，标注题目关键条件",
                    "辅助线缺失": f"建议加强几何作图训练，掌握常见辅助线构造方法",
                    "逻辑跳步": f"建议养成逐步书写的习惯，每步都要有理有据",
                    "知识缺失": f"建议从基础开始系统复习{node_name}",
                }
                specific = cause_advice.get(top_cause, "")
                if specific:
                    return f"{node_name}薄弱（{top_cause}占比{top_ratio:.0%}），{specific}"
        if root_cause and root_cause.get("contribution_ratio", 0) > 0.3:
            root_name = root_cause.get("root_name", "")
            return f"根源在于{root_name}基础不牢，建议先巩固{root_name}再突破{node_name}"
        return f"建议重点复习{node_name}相关知识，多做针对性练习"
