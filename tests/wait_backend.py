"""等待后端启动并健康检查"""
import time
import requests

for i in range(60):
    try:
        resp = requests.get("http://localhost:8000/api/health", timeout=3)
        if resp.status_code == 200:
            print(f"后端已启动 (尝试 {i+1} 次): {resp.json()}")
            break
    except Exception:
        pass
    time.sleep(2)
else:
    print("后端 120s 内未启动")
