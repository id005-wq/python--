import requests

r = requests.post(
    "https://api.deepseek.com/chat/completions",
    headers={"Authorization": "Bearer sk-b10d2961a7c54cc081a4353fe365550a"},
    json={
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": "你好"}]
    }
)
print(r.json()["choices"][0]["message"]["content"])