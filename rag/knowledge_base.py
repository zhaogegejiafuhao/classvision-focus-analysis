"""知识库构建模块：PDF解析 + 文本分块"""

import os
import re
from typing import List

import fitz  # pymupdf - 比pdfplumber更强大

from backend.core.config import settings


_knowledge_base: "KnowledgeBase | None" = None


def get_knowledge_base() -> "KnowledgeBase":
    """获取知识库单例（供 embedding_service 等模块复用，避免循环依赖）"""
    global _knowledge_base
    if _knowledge_base is None:
        _knowledge_base = KnowledgeBase()
    return _knowledge_base


class KnowledgeBase:
    """知识库管理"""

    def __init__(self):
        self.chunk_size = settings.RAG_CHUNK_SIZE
        self.chunk_overlap = settings.RAG_CHUNK_OVERLAP
        self.knowledge_dir = settings.RAG_KNOWLEDGE_DIR

        # 确保目录存在
        os.makedirs(self.knowledge_dir, exist_ok=True)

    def parse_pdf(self, file_path: str) -> str:
        """解析PDF文件，提取文本"""
        text = ""
        try:
            doc = fitz.open(file_path)
            for page in doc:
                page_text = page.get_text()
                if page_text:
                    text += page_text + "\n"
            doc.close()
        except Exception as e:
            print(f"PDF解析失败: {e}")
            return ""

        # 清理文本
        text = self._clean_text(text)
        return text

    def parse_txt(self, file_path: str) -> str:
        """解析TXT文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            print(f"TXT解析失败: {e}")
            return ""

        text = self._clean_text(text)
        return text

    def parse_md(self, file_path: str) -> str:
        """解析Markdown文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            print(f"Markdown解析失败: {e}")
            return ""

        # 保留Markdown格式，只清理多余空行
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text

    def parse_docx(self, file_path: str) -> str:
        """解析 Word 文档（.docx），提取段落和表格文本"""
        try:
            from docx import Document
            doc = Document(file_path)
            parts = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
            for table in doc.tables:
                for row in table.rows:
                    cells = [c.text.strip() for c in row.cells if c.text.strip()]
                    if cells:
                        parts.append(" | ".join(cells))
            text = "\n\n".join(parts)
        except Exception as e:
            print(f"DOCX解析失败: {e}")
            return ""
        return self._clean_text(text)

    def parse_pptx(self, file_path: str) -> str:
        """解析 PPT 课件（.pptx），按页提取文本和表格，保留页码"""
        try:
            from pptx import Presentation
            prs = Presentation(file_path)
            slides_text = []
            for i, slide in enumerate(prs.slides, 1):
                texts = []
                for shape in slide.shapes:
                    if shape.has_text_frame:
                        for para in shape.text_frame.paragraphs:
                            t = para.text.strip()
                            if t:
                                texts.append(t)
                    if shape.has_table:
                        for row in shape.table.rows:
                            cells = [c.text.strip() for c in row.cells if c.text.strip()]
                            if cells:
                                texts.append(" | ".join(cells))
                if texts:
                    slides_text.append(f"[第{i}页]\n" + "\n".join(texts))
            text = "\n\n".join(slides_text)
        except Exception as e:
            print(f"PPTX解析失败: {e}")
            return ""
        return self._clean_text(text)

    def _clean_text(self, text: str) -> str:
        """清理文本：只移除控制字符和多余空白，保留所有正常标点"""
        # 移除控制字符（保留 \n \t）
        text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)
        # 合并连续空格/制表符
        text = re.sub(r'[ \t]{2,}', ' ', text)
        # 合并多余空行
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    def split_into_chunks(self, text: str) -> List[str]:
        """将文本分块"""
        chunks = []

        # 按段落分割
        paragraphs = text.split('\n\n')

        current_chunk = ""
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue

            # 如果当前块 + 新段落 <= chunk_size，则合并
            if len(current_chunk) + len(para) + 2 <= self.chunk_size:
                current_chunk += "\n\n" + para if current_chunk else para
            else:
                # 当前块达到上限，保存
                if current_chunk:
                    chunks.append(current_chunk)

                # 如果段落本身超过chunk_size，需要进一步分割
                if len(para) > self.chunk_size:
                    # 按句子分割
                    sentences = re.split(r'[。！？\.\!\?]', para)
                    for sent in sentences:
                        sent = sent.strip()
                        if not sent:
                            continue
                        if len(sent) > self.chunk_size:
                            # 强制分割
                            for i in range(0, len(sent), self.chunk_size):
                                chunk_part = sent[i:i + self.chunk_size]
                                chunks.append(chunk_part)
                        else:
                            chunks.append(sent)
                else:
                    current_chunk = para

        # 保存最后一个块
        if current_chunk:
            chunks.append(current_chunk)

        # 添加重叠（可选）
        if self.chunk_overlap > 0 and len(chunks) > 1:
            overlapped_chunks = []
            for i, chunk in enumerate(chunks):
                if i > 0:
                    # 从前一个块的末尾取overlap部分
                    prev_overlap = chunks[i - 1][-self.chunk_overlap:]
                    chunk = prev_overlap + chunk
                overlapped_chunks.append(chunk)
            return overlapped_chunks

        return chunks

    def process_file(self, file_path: str) -> List[str]:
        """处理文件，返回文本块列表"""
        ext = os.path.splitext(file_path)[1].lower()

        if ext == '.pdf':
            text = self.parse_pdf(file_path)
        elif ext == '.txt':
            text = self.parse_txt(file_path)
        elif ext == '.md':
            text = self.parse_md(file_path)
        elif ext == '.docx':
            text = self.parse_docx(file_path)
        elif ext == '.pptx':
            text = self.parse_pptx(file_path)
        else:
            print(f"不支持的文件类型: {ext}")
            return []

        if not text:
            return []

        chunks = self.split_into_chunks(text)
        return chunks

    def index_history_reports(self, reports: List[str]) -> List[str]:
        """索引历史报告"""
        all_chunks = []
        for report in reports:
            if report:
                chunks = self.split_into_chunks(report)
                all_chunks.extend(chunks)
        return all_chunks