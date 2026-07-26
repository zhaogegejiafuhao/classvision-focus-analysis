"""pytest 全局配置

自动将项目根目录加入 sys.path，使测试可从任意目录运行。
替代各测试文件中硬编码的 sys.path.insert(0, "d:/ClassVision")。
"""
import sys
from pathlib import Path

# 项目根目录 = conftest.py 所在目录的父目录
_PROJECT_ROOT = str(Path(__file__).resolve().parent.parent)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)
