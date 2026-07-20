"""检查 Ollama 模型信息"""
import requests

r = requests.get("http://localhost:11434/api/tags", timeout=5)
data = r.json()
for m in data.get("models", []):
    details = m.get("details", {})
    print(f"{m['name']}: size={m.get('size', 0) // 1024 // 1024}MB, "
          f"params={details.get('parameter_size', '?')}, "
          f"quant={details.get('quantization_level', '?')}")
