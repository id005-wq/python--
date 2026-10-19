import requests

API_KEY = "sk-b10d2961a7c54cc081a4353fe365550a"

url = "https://api.deepseek.com/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "用一句话介绍 Python"}
    ]
}

r = requests.post(url, headers=headers, json=data)

print("状态码：", r.status_code)
print("回复：", r.json()["choices"][0]["message"]["content"])