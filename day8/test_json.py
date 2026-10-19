import os
import json
import requests
from dotenv import load_dotenv

load_dotenv(override=True)
API_KEY = os.getenv("DEEPSEEK_API_KEY")

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 注意这里的 response_format 和 system 提示词
data = {
    "model": "deepseek-chat",
    "response_format": {
        "type": "json_object"
    },
    "messages": [
        {
            "role": "system",
            "content": "你是一个信息提取助手，请严格以JSON格式输出，不要包含任何Markdown标记或其他解释文字。提取出姓名、年龄和职业。"
        },
        {
            "role": "user",
            "content": "我叫张三，今年25岁，是个软件工程师。"
        }
    ]
}

r = requests.post(url, headers=headers, json=data)
content = r.json()["choices"][0]["message"]["content"]

print("原始返回：", content)

# 把返回的 JSON 字符串转成 Python 字典
result = json.loads(content)
print("提取的名字：", result["name"])