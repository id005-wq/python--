with open("test.txt", "w", encoding="utf-8") as f:
    f.write("你好，Python\n")

with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

with open("test.txt", "a", encoding="utf-8") as f:
    f.write("你好，Python\n")
