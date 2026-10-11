# import requests
#
# r = requests.get("https://api.github.com")
# print(r.status_code)
# data = r.json()
# print(data)

# import requests
#
# r = requests.get("https://api.github.com/users/torvalds")
# print(r.status_code)
# data = r.json()
# print(data["name"])
# print(data["public_repos"])
# print(data["followers"])

import requests

r = requests.post("https://httpbin.org/post", data={"name": "张三", "age": 20})
print(r.status_code)
print(r.json())