"""RAG 多轮对话状态机：会话管理 + 上下文窗口 + 意图识别"""

import json
import logging
import re
from typing import List, Optional

from sqlalchemy.orm import Session

from backend.models.tables import RagConversation, RagMessage

logger = logging.getLogger("rag")

# 上下文窗口：最近 N 轮对话拼入 LLM prompt
MAX_CONTEXT_TURNS = 4

# 追问意图关键词
FOLLOWUP_PATTERNS = [
    r'^(那|那么|另外|还有|接着|然后|接下来)',
    r'(再详细|详细说说|展开说|具体说|详细讲|深入)',
    r'(是什么|什么意思|怎么理解|指的是)',
    r'(举个例子|例如|比如|实例)',
    r'(为什么|为何|原因)',
    r'(呢|吗|嘛|吧)\s*$',
    r'^(它|这|那|该|此)',
]


def is_followup(question: str, conversation: Optional[RagConversation]) -> bool:
    """判断是否为追问（基于关键词 + 会话历史）

    追问特征：
    1. 以"那/另外/还有"等转折词开头
    2. 包含"再详细/展开说"等深入请求
    3. 以"呢/吗/嘛"结尾的简短问句
    4. 指代词"它/这/那"开头
    5. 会话中有最近的 assistant 回答（上下文存在）
    """
    if not conversation or not conversation.messages:
        return False

    question = question.strip()
    if not question:
        return False

    # 关键词匹配
    for pattern in FOLLOWUP_PATTERNS:
        if re.search(pattern, question):
            logger.info("followup_detected question=%r pattern=%s", question, pattern)
            return True

    # 短问题（<8字）且有历史对话，大概率是追问
    if len(question) < 8:
        logger.info("followup_detected_short question=%r len=%d", question, len(question))
        return True

    return False


def build_context_messages(conversation: RagConversation, max_turns: int = MAX_CONTEXT_TURNS) -> List[dict]:
    """从会话历史构建上下文消息列表（最近 max_turns 轮）"""
    messages = []
    recent = conversation.messages[-(max_turns * 2):] if conversation.messages else []
    for msg in recent:
        messages.append({"role": msg.role, "content": msg.content})
    return messages


class ConversationService:
    """RAG 多轮对话状态机"""

    def __init__(self, db: Session):
        self.db = db

    def create_conversation(self, user_id: int, title: str = "新对话") -> RagConversation:
        """创建新会话"""
        conv = RagConversation(user_id=user_id, title=title, state="idle")
        self.db.add(conv)
        self.db.commit()
        self.db.refresh(conv)
        return conv

    def get_conversation(self, conv_id: int, user_id: int) -> Optional[RagConversation]:
        """获取会话（验证所有权）"""
        return self.db.query(RagConversation).filter(
            RagConversation.id == conv_id,
            RagConversation.user_id == user_id,
        ).first()

    def list_conversations(self, user_id: int) -> List[RagConversation]:
        """列出用户的所有会话"""
        return self.db.query(RagConversation).filter(
            RagConversation.user_id == user_id
        ).order_by(RagConversation.updated_at.desc()).all()

    def delete_conversation(self, conv_id: int, user_id: int) -> bool:
        """删除会话"""
        conv = self.get_conversation(conv_id, user_id)
        if not conv:
            return False
        self.db.query(RagMessage).filter(RagMessage.conversation_id == conv_id).delete()
        self.db.delete(conv)
        self.db.commit()
        return True

    def add_message(
        self,
        conversation_id: int,
        role: str,
        content: str,
        retrieved_chunks: list = None,
        is_followup_flag: bool = False,
    ) -> RagMessage:
        """添加消息到会话"""
        msg = RagMessage(
            conversation_id=conversation_id,
            role=role,
            content=content,
            retrieved_chunks=json.dumps(retrieved_chunks, ensure_ascii=False) if retrieved_chunks else None,
            is_followup=is_followup_flag,
        )
        self.db.add(msg)
        # 更新会话状态和时间
        conv = self.db.query(RagConversation).filter(RagConversation.id == conversation_id).first()
        if conv:
            conv.state = "answering" if role == "assistant" else "querying"
            # 用第一条用户消息作为标题
            if conv.title == "新对话" and role == "user":
                conv.title = content[:50]
        self.db.commit()
        self.db.refresh(msg)
        return msg

    def get_history(self, conversation_id: int, limit: int = 20) -> List[RagMessage]:
        """获取会话历史消息"""
        return self.db.query(RagMessage).filter(
            RagMessage.conversation_id == conversation_id
        ).order_by(RagMessage.id.desc()).limit(limit).all()[::-1]
