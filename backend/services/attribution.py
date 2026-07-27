"""
ClassVision 归因分析层（编排层）

本模块已拆分为三个子模块，此处仅做统一 re-export 以保持向后兼容：
- attribution_core：DecayPropagate 核心算法 + 共享数据结构（ErrorEvent/WeaknessResult/AnalysisReport）
- knowledge_attribution：知识归因（ErrorMapper + KnowledgeAttributionService + 单例）
- writing_attribution：写作归因（WritingAttributionService + 单例 + 写作数据结构）

外部代码可继续 `from backend.services.attribution import ...`，无需修改。
"""
from backend.services.attribution_core import (
    ErrorEvent,
    WeaknessResult,
    AnalysisReport,
    DecayPropagate,
)
from backend.services.knowledge_attribution import (
    ErrorMapper,
    KnowledgeAttributionService,
    knowledge_attribution_service,
)
from backend.services.writing_attribution import (
    WritingErrorEvent,
    WritingWeaknessResult,
    WritingAnalysisReport,
    WritingAttributionService,
    writing_attribution_service,
)

__all__ = [
    # 共享核心
    "ErrorEvent",
    "WeaknessResult",
    "AnalysisReport",
    "DecayPropagate",
    # 知识归因
    "ErrorMapper",
    "KnowledgeAttributionService",
    "knowledge_attribution_service",
    # 写作归因
    "WritingErrorEvent",
    "WritingWeaknessResult",
    "WritingAnalysisReport",
    "WritingAttributionService",
    "writing_attribution_service",
]
