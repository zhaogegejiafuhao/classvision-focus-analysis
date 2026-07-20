"""清理课堂 ID=10 的对话历史（测试累积导致历史混入）"""
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "classvision.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 查看当前对话历史数量
cursor.execute("SELECT COUNT(*) FROM chat_message WHERE classroom_id = 10")
count = cursor.fetchone()[0]
print(f"课堂 10 当前对话历史: {count} 条")

# 清理
cursor.execute("DELETE FROM chat_message WHERE classroom_id = 10")
conn.commit()
print(f"已清理 {count} 条对话历史")

# 验证
cursor.execute("SELECT COUNT(*) FROM chat_message WHERE classroom_id = 10")
count_after = cursor.fetchone()[0]
print(f"清理后: {count_after} 条")

conn.close()
