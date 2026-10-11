# x = input("What's x? ")
# y = input("What's y? ")
#
# z = x + y
#
# print(z)

# x = input("What's x? ")
# match x:
#     case 42| "forty-two":
#         print("Yes")
#     case _:
#         print("No")
class Student:
    def __init__(self, name, sid, scores):
        self.name = name
        self.sid = sid
        self.scores = scores

    def show_info(self):
        print("姓名：", self.name)
        print("学号：", self.sid)

    def average(self):
        return sum(self.scores) / len(self.scores)


class GraduateStudent(Student):
    def __init__(self, name, sid, scores, advisor):
        super().__init__(name, sid, scores)
        self.advisor = advisor

    def show_info(self):
        super().show_info()
        print("导师：", self.advisor)


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, stu):
        self.students.append(stu)

    def list_students(self):
        print("课程：", self.course_name)
        for s in self.students:
            print(s.name)

s1 = Student("张三", "2023001", [85, 90, 78])
s2 = Student("李四", "2023002", [70, 80, 90])

s1.show_info()
print("平均分：", s1.average())

g1 = GraduateStudent("王五", "2023003", [88, 92, 85], "赵教授")
g1.show_info()
print("平均分：", g1.average())

c = Course("Python 程序设计")
c.add_student(s1)
c.add_student(s2)
c.add_student(g1)
c.list_students()