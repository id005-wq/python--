from fastapi import FastAPI
import pymysql
import pymysql.cursors
from pydantic import BaseModel
class Student(BaseModel):
    name: str
    sid: str
    score: int

app = FastAPI()

def get_conn():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="test_db",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get("/students")
def list_students():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.close()
    return results

@app.post("/students")
def create_student(student: Student):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, sid, score) VALUES (%s, %s, %s)",
        (student.name, student.sid, student.score)
    )
    conn.commit()
    conn.close()
    return {"message": "创建成功", "student": student}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    result = cursor.fetchone()
    conn.close()
    return result

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    conn.close()
    return {"message": "删除成功", "student_id": student_id}

@app.put("/students/{student_id}")

def update_student(student_id: int, student: Student):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name = %s, sid = %s, score = %s WHERE id = %s",
        (student.name, student.sid, student.score, student_id)
    )
    conn.commit()
    conn.close()
    return {"message": "更新成功", "student": student}
