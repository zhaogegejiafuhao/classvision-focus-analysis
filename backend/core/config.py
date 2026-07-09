from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "ClassVision"
    DATABASE_URL: str = "sqlite:///./classvision.db"
    OLLAMA_HOST: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "qwen3:4b"

    # RAG配置
    RAG_CACHE_DIR: str = "D:/models/sentence-transformers"  # 嵌入模型缓存目录
    RAG_INDEX_DIR: str = "D:/ClassVision/data/rag_index"  # FAISS索引目录
    RAG_KNOWLEDGE_DIR: str = "D:/ClassVision/data/knowledge"  # 知识库文档目录
    RAG_EMBEDDING_MODEL: str = "paraphrase-multilingual-MiniLM-L12-v2"  # 嵌入模型
    RAG_CHUNK_SIZE: int = 500  # 文本块大小（字符）
    RAG_CHUNK_OVERLAP: int = 50  # 文本块重叠
    RAG_TOP_K: int = 5  # 检索返回top-k结果

    # 试卷扫描配置
    PAPER_UPLOAD_DIR: str = "D:/ClassVision/data/papers"  # 试卷图片存储目录
    PAPER_IMAGE_WIDTH: int = 1000  # 透视矫正后的标准宽度（像素）

    class Config:
        env_file = ".env"


settings = Settings()
