"""
知识归因服务（从 attribution.py 拆分）

基于数学知识图谱（KnowledgeGraph）的错题归因分析：
- ErrorMapper：错题文本 → 知识图谱节点的双通道映射（关键词规则 + LLM语义匹配）
- KnowledgeAttributionService：对外统一接口，调用 DecayPropagate 生成学情报告
"""
import logging
from datetime import date

logger = logging.getLogger(__name__)

from backend.services.knowledge_graph import KnowledgeGraph
from backend.services.attribution_core import (
    DecayPropagate,
    ErrorEvent,
    WeaknessResult,
    AnalysisReport,
)


class ErrorMapper:
    """错题映射双通道：关键词规则 + LLM语义匹配"""

    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg

    def map_by_keywords(self, error_text: str) -> list[str]:
        """通道1：关键词规则匹配"""
        matched = self.kg.search_by_keywords(error_text)
        if matched:
            logger.debug(f"[ErrorMapper] 关键词规则命中: {error_text[:30]}... → {[self.kg.get_node(m)['name'] for m in matched if self.kg.get_node(m)]}")
        return matched

    def auto_expand_rules(self, error_text: str, original_match: str, corrected_match: str) -> bool:
        """
        规则库自进化：当教师将LLM匹配的知识点修正为另一知识点时，
        自动提取错题中的关键词加入修正后知识点的规则集

        Args:
            error_text: 错题原文
            original_match: LLM原始匹配的知识点ID
            corrected_match: 教师修正后的知识点ID

        Returns:
            是否成功扩展了规则
        """
        if original_match == corrected_match:
            return False

        # 从错题文本中提取关键词（简单的分词策略）
        import re
        # 提取2-4字的中文词组
        chinese_words = re.findall(r'[\u4e00-\u9fa5]{2,4}', error_text)

        # 获取修正后知识点的现有关键词
        corrected_node = self.kg.get_node(corrected_match)
        if not corrected_node:
            return False

        existing_keywords = set(corrected_node.get("keywords", []))

        # 找出与原始匹配知识点关键词的交集（即可能导致误匹配的关键词）
        original_node = self.kg.get_node(original_match)
        original_keywords = set(original_node.get("keywords", [])) if original_node else set()

        # 从错题中提取的关键词中，排除原始匹配的关键词
        new_keywords = []
        for word in chinese_words:
            if word not in existing_keywords and word not in original_keywords:
                # 检查这个词是否在错题中有意义（不是常见停用词）
                stop_words = {"已知", "求", "设", "则", "因为", "所以", "且", "或", "若", "则"}
                if word not in stop_words:
                    new_keywords.append(word)

        # 添加最有意义的1-2个关键词
        added = []
        for kw in new_keywords[:2]:
            existing_keywords.add(kw)
            added.append(kw)

        if added:
            # 更新知识图谱中的关键词
            self.kg._nodes[corrected_match]["keywords"] = list(existing_keywords)
            logger.info(f"[ErrorMapper] 规则自进化: 知识点'{corrected_node['name']}'新增关键词: {added}")
            return True

        return False

    async def map_by_llm(self, error_text: str, subject: str = "math") -> list[str]:
        """通道2：LLM语义匹配"""
        from backend.services.llm_utils import parse_llm_json
        from backend.services import async_llm

        # 获取所有知识点名称供LLM选择
        all_nodes = self.kg.get_all_nodes()
        node_names = {nid: node["name"] for nid, node in all_nodes.items() if node["level"] >= 2}
        node_list = "\n".join([f"- {nid}: {name}" for nid, name in node_names.items()])

        prompt = f"""以下是一道数学错题，请判断它涉及的知识点。

## 错题内容
{error_text}

## 可选知识点列表
{node_list}

请从上述列表中选择最相关的1-3个知识点ID，输出JSON格式：
{{"matched": ["知识点ID1", "知识点ID2"]}}

只输出JSON，不要输出其他内容。"""

        try:
            messages = [{"role": "user", "content": prompt}]
            data = await async_llm.async_chat_json(
                messages=messages,
                mode="deep",
                temperature=0.1,
                max_tokens=256,
            )
            return [mid for mid in data.get("matched", []) if mid in all_nodes]
        except Exception:
            pass

        return []

    async def map_error(self, error_text: str) -> list[str]:
        """双通道融合映射：关键词命中→直接采用；未命中→LLM兜底"""
        keyword_matches = self.map_by_keywords(error_text)
        if keyword_matches:
            return keyword_matches

        llm_matches = await self.map_by_llm(error_text)
        return llm_matches


class KnowledgeAttributionService:
    """知识归因服务 - 对外统一接口"""

    def __init__(self, kg: KnowledgeGraph | None = None, wkg: 'WritingKnowledgeGraph | None' = None):
        self.kg = kg or KnowledgeGraph()
        self.decay_propagate = DecayPropagate(self.kg)
        self.error_mapper = ErrorMapper(self.kg)
        self.wkg = wkg

    async def analyze(
        self,
        errors: list[ErrorEvent],
        reference_date: date | None = None,
        correction_records: list[dict] | None = None,
    ) -> AnalysisReport:
        """执行完整的知识归因分析"""

        # Step 1: DecayPropagate薄弱度计算
        weak_points = self.decay_propagate.analyze(errors, reference_date, correction_records=correction_records)

        # Step 2: 生成雷达图数据（一级维度）
        radar = {}
        radar_dims = self.kg.get_radar_dimensions()
        for dim in radar_dims:
            dim_id = dim["id"]
            dim_name = dim["name"]
            # 计算该维度下所有子节点的最大薄弱度
            max_weakness = 0.0
            for wp in weak_points:
                # 检查wp是否属于该维度
                node = self.kg.get_node(wp.knowledge_id)
                if node and self._is_under_dimension(wp.knowledge_id, dim_id):
                    max_weakness = max(max_weakness, wp.weakness_score)
            # 雷达图显示"掌握度"而非"薄弱度"，所以用1-薄弱度
            radar[dim_name] = round(1.0 - max_weakness, 2)

        # Step 3: 统计订正状态（PoC阶段简化）
        total_errors = len(errors)
        corrected = sum(1 for e in errors if e.error_weight < 1.0)

        return AnalysisReport(
            student_id="",
            analysis_date=(reference_date or date.today()).isoformat(),
            radar=radar,
            weak_points=weak_points,
            correction_status={
                "total_errors": total_errors,
                "corrected": corrected,
                "uncorrected": total_errors - corrected,
                "correction_rate": round(corrected / total_errors, 2) if total_errors > 0 else 0.0,
            },
        )

    def _is_under_dimension(self, node_id: str, dimension_id: str) -> bool:
        """检查node_id是否属于dimension_id的子树"""
        if node_id == dimension_id:
            return True
        ancestors = self.kg.get_ancestors(node_id)
        return dimension_id in ancestors


# ===== 模块级单例 =====
knowledge_attribution_service = KnowledgeAttributionService()
