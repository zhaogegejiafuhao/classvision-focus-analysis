"""结构化日志配置

提供两种日志格式：
1. 开发模式（默认）：彩色可读格式
2. 生产模式（JSON_FORMAT=true）：JSON 格式，便于 ELK/Loki 等日志系统采集

使用方式：
    from backend.core.logging_config import setup_logging
    setup_logging()

或在 main.py 启动时调用。
"""

import json
import logging
import os
import sys
from datetime import datetime


class JSONFormatter(logging.Formatter):
    """JSON 格式日志格式器，便于日志聚合系统采集"""

    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        # 异常信息
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)

        # 额外字段（logger.info("msg", extra={...})）
        for key, value in record.__dict__.items():
            if key not in {
                "name", "msg", "args", "levelname", "levelno", "pathname",
                "filename", "module", "exc_info", "exc_text", "stack_info",
                "lineno", "funcName", "created", "msecs", "relativeCreated",
                "thread", "threadName", "processName", "process", "message",
                "taskName",
            } and not key.startswith("_"):
                try:
                    json.dumps(value)
                    log_entry[key] = value
                except (TypeError, ValueError):
                    log_entry[key] = str(value)

        return json.dumps(log_entry, ensure_ascii=False)


class DevFormatter(logging.Formatter):
    """开发模式彩色格式器"""

    COLORS = {
        "DEBUG": "\033[36m",     # 青色
        "INFO": "\033[32m",      # 绿色
        "WARNING": "\033[33m",   # 黄色
        "ERROR": "\033[31m",     # 红色
        "CRITICAL": "\033[35m",  # 紫色
    }
    RESET = "\033[0m"

    def format(self, record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelname, "")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = record.getMessage()

        # 简短模块名
        module = record.name
        if module.startswith("backend."):
            module = module[8:]
        if module.startswith("uvicorn"):
            module = "uvicorn"

        line = f"{timestamp} {color}{record.levelname:<8}{self.RESET} [{module}] {msg}"

        if record.exc_info:
            line += "\n" + self.formatException(record.exc_info)

        return line


def setup_logging():
    """初始化全局日志配置

    环境变量：
        JSON_FORMAT=true  使用 JSON 格式（生产环境）
        LOG_LEVEL=DEBUG   日志级别（默认 INFO）
    """
    use_json = os.getenv("JSON_FORMAT", "false").lower() in ("true", "1", "yes")
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    formatter = JSONFormatter() if use_json else DevFormatter()

    # 配置根 logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    # 清除已有 handler（避免重复日志）
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    # 调整第三方库日志级别
    logging.getLogger("uvicorn").setLevel(log_level)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)  # access log 太吵
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)

    # 确保 RAG logger 也用新格式
    rag_logger = logging.getLogger("rag")
    rag_logger.handlers.clear()
    rag_logger.addHandler(handler)
    rag_logger.setLevel(log_level)
    rag_logger.propagate = False  # 避免重复输出

    return root_logger
