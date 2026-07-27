"""
写作归因服务（从 attribution.py 拆分）

复用 DecayPropagate 核心算法，但基于写作能力图谱（WritingKnowledgeGraph）：
将写作错因标签（素材匮乏、逻辑断层等）映射到 DAG 节点后，
进行后向传播与前向聚合分析，生成"写作能力雷达"维度的学情报告。
"""
import logging
from datetime import date
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

from backend.services.attribution_core import (
    DecayPropagate,
    ErrorEvent,
    WeaknessResult,
)
from backend.services.writing_graph import (
    WritingKnowledgeGraph,
    WRITING_ERROR_CAUSE_MAPPING,
    WRITING_ERROR_CAUSE_FINE_MAPPING,
    WRITING_ERROR_SUGGESTIONS,
)


@dataclass
class WritingErrorEvent:
    """写作错因事件"""
    error_cause: str         # 错因标签：素材匮乏|逻辑断层|修辞单一|偏题跑题|书写潦草
    error_weight: float      # 错误严重度 1.0=严重, 0.5=轻微
    timestamp: date          # 错误发生日期
    essay_title: str = ""    # 作文题目（用于展示）


@dataclass
class WritingWeaknessResult:
    """写作单项薄弱度结果"""
    dimension_id: str        # 一级维度ID（theme/structure/expression/writing_norm）
    dimension_name: str      # 维度名称
    weakness_score: float    # 归一化薄弱度 [0, 1]
    sub_weaknesses: list[dict] = field(default_factory=list)  # 子能力薄弱详情
    error_causes: list[str] = field(default_factory=list)     # 涉及的错因标签
    suggestion: str = ""


@dataclass
class WritingAnalysisReport:
    """写作学情分析报告"""
    student_id: str
    analysis_date: str
    radar: dict[str, float]                  # 一级维度 → 掌握度 (1 - 薄弱度)
    weak_dimensions: list[WritingWeaknessResult]
    error_cause_distribution: dict[str, int] # 错因标签出现次数统计
    overall_suggestion: str = ""


class WritingAttributionService:
    """
    写作归因服务 - 复用 DecayPropagate 算法但使用 WritingKnowledgeGraph

    将写作错因标签（素材匮乏、逻辑断层等）映射到 DAG 节点后，
    调用 DecayPropagate 进行后向传播与前向聚合分析，
    最终生成"写作能力雷达"维度的学情报告。
    """

    def __init__(self, wkg: WritingKnowledgeGraph | None = None):
        self.wkg = wkg or WritingKnowledgeGraph()
        self.decay_propagate = DecayPropagate(self.wkg)

    async def analyze(
        self,
        writing_errors: list[WritingErrorEvent],
        student_id: str = "",
        reference_date: date | None = None,
    ) -> WritingAnalysisReport:
        """
        执行写作归因分析

        Args:
            writing_errors: 写作错因事件列表
            student_id: 学生ID
            reference_date: 参考日期（默认今天）

        Returns:
            WritingAnalysisReport 写作学情分析报告
        """
        if reference_date is None:
            reference_date = date.today()

        # Step 1: 将写作错因标签映射为 DAG 节点的 ErrorEvent 列表
        mapped_errors: list[ErrorEvent] = []
        error_cause_counts: dict[str, int] = {}

        for we in writing_errors:
            cause = we.error_cause
            error_cause_counts[cause] = error_cause_counts.get(cause, 0) + 1

            # 细粒度映射：一个错因可能对应多个DAG节点
            node_ids = WritingKnowledgeGraph.map_error_cause_to_nodes(cause)
            if not node_ids:
                # 回退到一级维度映射
                dim_id = WritingKnowledgeGraph.map_error_cause_to_dimension(cause)
                if dim_id:
                    node_ids = [dim_id]

            for node_id in node_ids:
                mapped_errors.append(ErrorEvent(
                    knowledge_node_id=node_id,
                    error_weight=we.error_weight / len(node_ids),  # 分摊权重
                    timestamp=we.timestamp,
                    question_content=we.essay_title[:50],
                    error_cause=cause,
                ))

        if not mapped_errors:
            # 没有可映射的错因，返回空报告
            radar_dims = self.wkg.get_radar_dimensions()
            empty_radar = {dim["name"]: 1.0 for dim in radar_dims}
            return WritingAnalysisReport(
                student_id=student_id,
                analysis_date=reference_date.isoformat(),
                radar=empty_radar,
                weak_dimensions=[],
                error_cause_distribution=error_cause_counts,
                overall_suggestion="暂无写作错因数据，继续保持良好的写作习惯",
            )

        # Step 2: 调用 DecayPropagate 进行薄弱度分析
        weak_points = self.decay_propagate.analyze(
            errors=mapped_errors,
            reference_date=reference_date,
            top_k=20,  # 写作图谱节点少，取全部
        )

        # Step 3: 生成写作能力雷达（一级维度）
        radar = {}
        radar_dims = self.wkg.get_radar_dimensions()
        for dim in radar_dims:
            dim_id = dim["id"]
            dim_name = dim["name"]
            # 该维度下所有子节点的最大薄弱度
            max_weakness = 0.0
            for wp in weak_points:
                if self._is_under_dimension(wp.knowledge_id, dim_id):
                    max_weakness = max(max_weakness, wp.weakness_score)
            # 雷达图展示"掌握度"而非"薄弱度"
            radar[dim_name] = round(1.0 - max_weakness, 2)

        # Step 4: 按一级维度聚合薄弱结果
        weak_dimensions = self._aggregate_by_dimension(
            weak_points, error_cause_counts
        )

        # Step 5: 生成综合建议
        overall_suggestion = self._generate_overall_suggestion(
            radar, error_cause_counts
        )

        return WritingAnalysisReport(
            student_id=student_id,
            analysis_date=reference_date.isoformat(),
            radar=radar,
            weak_dimensions=weak_dimensions,
            error_cause_distribution=error_cause_counts,
            overall_suggestion=overall_suggestion,
        )

    def _is_under_dimension(self, node_id: str, dimension_id: str) -> bool:
        """检查node_id是否属于dimension_id的子树"""
        if node_id == dimension_id:
            return True
        ancestors = self.wkg.get_ancestors(node_id)
        return dimension_id in ancestors

    def _aggregate_by_dimension(
        self,
        weak_points: list[WeaknessResult],
        error_cause_counts: dict[str, int],
    ) -> list[WritingWeaknessResult]:
        """按一级维度聚合薄弱结果"""
        dim_data: dict[str, dict] = {}

        for wp in weak_points:
            # 找到该节点所属的一级维度
            node = self.wkg.get_node(wp.knowledge_id)
            if not node:
                continue

            # 向上追溯到一级维度
            dim_id = wp.knowledge_id
            current = node
            while current.get("parent_id") and current.get("parent_id") != "root":
                dim_id = current["parent_id"]
                current = self.wkg.get_node(dim_id)

            if current.get("parent_id") != "root":
                # 本身就是一级维度
                if node.get("parent_id") == "root":
                    dim_id = wp.knowledge_id
                else:
                    continue

            if dim_id not in dim_data:
                dim_node = self.wkg.get_node(dim_id)
                dim_data[dim_id] = {
                    "dimension_name": dim_node["name"] if dim_node else dim_id,
                    "weakness_score": 0.0,
                    "sub_weaknesses": [],
                    "error_causes": set(),
                }

            # 更新维度薄弱度（取最大值）
            dim_data[dim_id]["weakness_score"] = max(
                dim_data[dim_id]["weakness_score"], wp.weakness_score
            )

            # 收集子能力薄弱详情
            dim_data[dim_id]["sub_weaknesses"].append({
                "node_id": wp.knowledge_id,
                "node_name": wp.knowledge_name,
                "weakness_score": wp.weakness_score,
                "error_count": wp.error_count,
                "error_cause_distribution": wp.error_cause_distribution,
                "root_cause": wp.root_cause,
            })

            # 收集该维度涉及的错因标签
            for cause in wp.error_cause_distribution:
                dim_data[dim_id]["error_causes"].add(cause)

        # 构建结果列表
        results = []
        for dim_id, data in dim_data.items():
            # 生成该维度的建议
            suggestion = self._generate_dimension_suggestion(
                dim_id, data["error_causes"], data["weakness_score"]
            )

            results.append(WritingWeaknessResult(
                dimension_id=dim_id,
                dimension_name=data["dimension_name"],
                weakness_score=round(data["weakness_score"], 4),
                sub_weaknesses=sorted(
                    data["sub_weaknesses"],
                    key=lambda x: x["weakness_score"],
                    reverse=True,
                ),
                error_causes=sorted(data["error_causes"]),
                suggestion=suggestion,
            ))

        # 按薄弱度降序排列
        results.sort(key=lambda r: r.weakness_score, reverse=True)
        return results

    @staticmethod
    def _generate_dimension_suggestion(
        dimension_id: str,
        error_causes: set[str],
        weakness_score: float,
    ) -> str:
        """生成单个维度的改进建议"""
        if not error_causes:
            return ""

        # 取最主要的错因标签
        main_cause = sorted(error_causes)[0]
        base_suggestion = WRITING_ERROR_SUGGESTIONS.get(main_cause, "")

        dim_names = {
            "theme": "审题立意",
            "structure": "结构组织",
            "expression": "语言表达",
            "writing_norm": "书写规范",
        }
        dim_name = dim_names.get(dimension_id, dimension_id)

        if weakness_score > 0.7:
            prefix = f"{dim_name}方面存在明显薄弱（{','.join(error_causes)}），需重点突破。"
        elif weakness_score > 0.4:
            prefix = f"{dim_name}方面有提升空间（{','.join(error_causes)}），建议针对性练习。"
        else:
            prefix = f"{dim_name}方面表现尚可，但仍需注意{','.join(error_causes)}问题。"

        return f"{prefix}{base_suggestion}" if base_suggestion else prefix

    @staticmethod
    def _generate_overall_suggestion(
        radar: dict[str, float],
        error_cause_counts: dict[str, int],
    ) -> str:
        """生成综合建议"""
        if not radar:
            return "暂无数据"

        # 找出最薄弱的维度
        sorted_dims = sorted(radar.items(), key=lambda x: x[1])
        weakest_dim = sorted_dims[0]

        # 找出出现最多的错因
        if error_cause_counts:
            top_cause = max(error_cause_counts, key=error_cause_counts.get)
            top_suggestion = WRITING_ERROR_SUGGESTIONS.get(top_cause, "")
        else:
            top_cause = ""
            top_suggestion = ""

        if weakest_dim[1] < 0.5:
            overall = (
                f"写作能力整体有待加强，最薄弱维度为'{weakest_dim[0]}'"
                f"（掌握度{weakest_dim[1]:.0%}），"
            )
        elif weakest_dim[1] < 0.8:
            overall = (
                f"写作能力总体中等，'{weakest_dim[0]}'维度需提升"
                f"（掌握度{weakest_dim[1]:.0%}），"
            )
        else:
            overall = "写作能力整体良好，各维度掌握度较高，"

        if top_cause:
            overall += f"最突出的问题是'{top_cause}'（出现{error_cause_counts[top_cause]}次）。"
        else:
            overall += "继续巩固提升。"

        if top_suggestion:
            overall += f"\n{top_suggestion}"

        return overall


# ===== 模块级单例 =====
writing_attribution_service = WritingAttributionService()
