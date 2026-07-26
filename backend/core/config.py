from pathlib import Path

from pydantic_settings import BaseSettings

# 项目根目录（始终指向 ClassVision/）
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    APP_NAME: str = "ClassVision"
    # 数据库路径：使用绝对路径，避免因启动目录不同导致指向不同 db
    DATABASE_URL: str = f"sqlite:///{PROJECT_ROOT / 'classvision.db'}"
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen3:4b"  # Ollama 深度模型
    OLLAMA_MODEL_FAST: str = "qwen2.5:3b"  # Ollama 快速模型

    # LLM Provider 配置（统一适配层，支持 Ollama / OpenRouter / DashScope / DeepSeek 等）
    LLM_PROVIDER: str = "ollama"  # ollama / openrouter / dashscope / deepseek / siliconflow / custom
    LLM_API_KEY: str = ""  # 云端 API Key（Ollama 不需要）
    LLM_BASE_URL: str = ""  # 云端 API Base URL（为空时使用预置值）
    LLM_MODEL: str = ""  # 云端主模型名（如 tencent/hunyuan-3、qwen-plus）
    LLM_MODEL_FAST: str = ""  # 云端快速模型名（为空时回退到 LLM_MODEL）
    LLM_MODEL_STRONG: str = ""  # 强模型名（用于几何题/复杂证明题，为空时默认 Qwen2.5-32B-Instruct）

    # RAG配置
    RAG_CACHE_DIR: str = str(PROJECT_ROOT / "models" / "sentence-transformers")  # 嵌入模型缓存目录
    RAG_INDEX_DIR: str = str(PROJECT_ROOT / "data" / "rag_index")  # FAISS索引目录
    RAG_KNOWLEDGE_DIR: str = str(PROJECT_ROOT / "data" / "knowledge")  # 知识库文档目录
    RAG_EMBEDDING_MODEL: str = "paraphrase-multilingual-MiniLM-L12-v2"  # 嵌入模型
    # --- 分块配置（WeKnora 文档分块指南 + Vecta 基准） ---
    RAG_CHUNK_BY_TOKENS: bool = False  # False=按字符计数（与 WeKnora/Vecta 一致）
    RAG_CHUNK_SIZE: int = 512  # 分块大小（字符数）— Vecta 50篇论文基准推荐值
    RAG_CHUNK_OVERLAP: int = 80  # 分块重叠（≈15%，WeKnora 默认 80 字符）
    RAG_CHUNK_STRATEGY: str = "auto"  # 分块策略：auto/heading/heuristic/legacy
    RAG_CHUNK_SEPARATORS: list = ["\n\n", "\n", "。", "！", "？", ";", "；"]  # 递归分隔符优先级
    RAG_EMBEDDING_TOKEN_LIMIT: int = 200  # 嵌入模型 Token 上限（MiniLM=256，设80%=200）
    # --- 父子分块（双层检索）---
    RAG_PARENT_CHILD_ENABLED: bool = True  # 开启父子分块
    RAG_PARENT_CHUNK_SIZE: int = 4096  # 父分块大小（字符数，给 LLM 完整上下文）
    RAG_CHILD_CHUNK_SIZE: int = 384  # 子分块大小（字符数，精准匹配）
    RAG_TOP_K: int = 5  # 检索返回top-k结果
    RAG_RERANKER_ENABLED: bool = False  # Cross-Encoder 重排开关（首次使用需下载 ~2GB 模型）
    RAG_RERANKER_MODEL: str = "BAAI/bge-reranker-v2-m3"  # 重排模型
    RAG_RERANKER_TOP_K: int = 3  # 重排后送入 LLM 的 chunk 数量
    RAG_RERANKER_MAX_CANDIDATES: int = 10  # 重排最大候选数量（CPU 模式 10 个约 17s，20 个约 33s）
    # 重排器运行设备：cpu 避免 4GB 显存 OOM（bge-reranker-v2-m3 ~2GB + qwen3:4b 2.4GB > 4GB VRAM）
    RAG_RERANKER_DEVICE: str = "cpu"
    # HyDE 查询改写：对短口语 query 调用 LLM 生成假答案文档做检索（默认关闭，每次多一轮 LLM 调用）
    RAG_HYDE_ENABLED: bool = False
    RAG_HYDE_MIN_QUERY_LEN: int = 10  # query 长度 < 此值才启用 HyDE
    RAG_HYDE_MAX_TOKENS: int = 200  # 假答案最大长度
    # 查询路由器：基于规则分流到不同检索链路（Tier1 直接 LLM / Tier2 BM25 / Tier3 Dense / Tier4 混合）
    RAG_QUERY_ROUTER_ENABLED: bool = True
    # Multi-Query/RAG-Fusion：对中等长度 query 生成多个视角变体，多路检索后 RRF 融合
    RAG_MULTI_QUERY_ENABLED: bool = False
    RAG_MULTI_QUERY_COUNT: int = 3  # 生成的变体数量（不含原始 query）
    RAG_MULTI_QUERY_MIN_LEN: int = 10  # query 长度 >= 此值才启用
    RAG_MULTI_QUERY_MAX_LEN: int = 100  # query 长度 <= 此值才启用

    # OJ 判题机配置
    OJ_JUDGER_URL: str = "http://127.0.0.1:12345"  # judger 容器映射地址

    # ===== AI 智能批改配置（ZhiReviewPi迁移） =====
    # 百度手写OCR
    BAIDU_OCR_API_KEY: str = ""
    BAIDU_OCR_SECRET_KEY: str = ""
    # 火山引擎豆包（多模态VL降级）
    VOLCENGINE_API_KEY: str = ""
    VOLCENGINE_BASE_URL: str = "https://ark.cn-beijing.volces.com/api/v3"
    DOUBAO_ENDPOINT_ID: str = ""
    # 批改引擎参数
    GRADING_LOW_CONFIDENCE_THRESHOLD: float = 0.7   # OCR低置信度阈值
    GRADING_ACCURACY_THRESHOLD: float = 0.8          # 模型准确率阈值（低于此值自动切换）
    GRADING_RUBRIC_CACHE_SIZE: int = 500              # Rubric LRU缓存容量

    # JWT 认证配置
    JWT_SECRET_KEY: str = ""  # 必须通过环境变量设置，留空则启动时生成随机密钥
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_HOURS: int = 24

    # 速率限制配置（防止 LLM 路由被滥用）
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_GLOBAL: str = "120/minute"       # 全局每分钟请求数
    RATE_LIMIT_LLM: str = "20/minute"           # LLM 相关路由（更严格）
    RATE_LIMIT_AUTH: str = "10/minute"          # 登录/注册路由（防暴力破解）

    # CORS 配置
    CORS_ORIGINS: str = "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173"  # 逗号分隔的允许源

    class Config:
        env_file = ".env"

    @property
    def cors_origins_list(self) -> list[str]:
        """将逗号分隔的 CORS_ORIGINS 转为列表"""
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]


settings = Settings()

# JWT 密钥自动生成：若环境变量未设置则生成随机密钥（每次重启后旧 token 失效）
if not settings.JWT_SECRET_KEY:
    import secrets
    settings.JWT_SECRET_KEY = secrets.token_urlsafe(32)
    import logging
    logging.getLogger("uvicorn").warning("JWT_SECRET_KEY 未设置，已自动生成随机密钥（重启后旧 token 将失效，请通过环境变量配置固定密钥）")
