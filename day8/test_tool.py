import os
import json
import requests
from dotenv import load_dotenv

load_dotenv(override=True)
API_KEY = os.getenv("DEEPSEEK_API_KEY")


def get_weather(city):
    return f"{city}今天天气晴朗，气温25度。"


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询指定城市的天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名称"}
                },
                "required": ["city"]
            }
        }
    }
]

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

messages = [
    {"role": "user", "content": "帮我查一下北京今天天气怎么样？"}
]

# 1. 第一次请求：发给 AI
data = {
    "model": "deepseek-chat",
    "messages": messages,
    "tools": tools
}
r = requests.post(url, headers=headers, json=data)
response = r.json()

# 2. 拿到 AI 的“工具调用请求”
message = response["choices"][0]["message"]
messages.append(message)  # 把 AI 的请求加进历史

# 3. 解析 AI 请求的参数，执行我们本地的函数
tool_call = message["tool_calls"][0]
function_name = tool_call["function"]["name"]
arguments = json.loads(tool_call["function"]["arguments"])

if function_name == "get_weather":
    city = arguments["city"]
    weather_result = get_weather(city)  # 真正调用本地函数
    print(f"【本地代码执行】查询到：{weather_result}")

    # 4. 把执行结果加进历史，发给 AI
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call["id"],
        "content": weather_result
    })

    # 5. 第二次请求：AI 拿到数据后，生成最终回复
    data2 = {
        "model": "deepseek-chat",
        "messages": messages
    }
    r2 = requests.post(url, headers=headers, json=data2)
    final_reply = r2.json()["choices"][0]["message"]["content"]

    print("\n【AI 最终回复】")
    print(final_reply)