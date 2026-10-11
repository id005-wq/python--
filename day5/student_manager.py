import json

FILE = "students.json"

def load_students():
    # 从文件读学生列表，文件不存在就返回 []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    ...


def save_students(students):
    # 把学生列表写入文件
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
    ...

def add_student(students):
    # 输入姓名、学号、成绩，加入列表
    name=input("请输入姓名：")
    sid=input("请输入学号：")
    scores=[int(score) for score in input("请输入成绩：").split()]
    students.append({"name": name, "sid": sid, "scores": scores})

    ...

def list_students(students):
    # 打印所有学生
    for student in students:
        print(f"姓名：{student['name']}, 学号：{student['sid']}, 成绩：{student['scores']}")



    ...

def find_students(students):
    # 输入学号，找到并打印
    sids_str = input("请输入学号（多个用逗号分隔）：")
    sids = sids_str.split(",")
    found = False

    for student in students:
        if student['sid'] in sids:
            print(f"找到学生：姓名：{student['name']}, 学号：{student['sid']}, 成绩：{student['scores']}")
            found = True
    if not found:
        print("未找到学生")
    ...

def delete_students(students):
    sids_str = input("请输入学号（多个用逗号分隔）：")
    sids = sids_str.split(",")

    new_students = [s for s in students if s['sid'] not in sids]

    removed = len(students) - len(new_students)
    students.clear()
    students.extend(new_students)

    print(f"删除了 {removed} 个")
    ...
# if __name__ == "__main__":
#     students = load_students()
#     print("初始学生：", students)
#
#     # 输入学号，找到并打印
#     find_students(students)
#
#     # 删除
#     delete_students(students)
#
#     save_students(students)

def main():
    students = load_students()      # 启动时读文件

    while True:
        print("\n1. 添加学生")
        print("2. 查看所有学生")
        print("3. 查找学生")
        print("4. 删除学生")
        print("5. 保存")
        print("6. 退出")

        choice = input("请选择：")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            list_students(students)
        elif choice == "3":
            find_students(students)
        elif choice == "4":
            delete_students(students)
        elif choice == "5":
            save_students(students)
            print("已保存")
        elif choice == "6":
            save_students(students)
            print("已保存，退出")
            break
        else:
            print("无效选择")

if __name__ == "__main__":
    main()

