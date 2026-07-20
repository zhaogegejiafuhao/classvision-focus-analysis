import requests
try:
    r = requests.get("http://127.0.0.1:11434/api/tags", timeout=10)
    print("Ollama OK, status:", r.status_code)
    print(r.text[:400])
except Exception as e:
    print("Ollama FAILED:", e)
