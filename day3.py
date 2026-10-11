# import json
#
# data = {"name": "张三", "age": 20, "scores": [85, 90]}
#
# # 写入
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)
#
# # 读取
# with open("data.json", "r", encoding="utf-8") as f:
#     loaded = json.load(f)
#     print(loaded)
#     print(loaded["name"])

# import requests
#
# r = requests.get("https://api.github.com")
# print(r.status_code)
from mytools import add, mul

print(add(2, 3))
print(mul(4, 5))
