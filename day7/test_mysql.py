import pymysql
import pymysql.cursors

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    database="test_db",
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

# 1. 建表
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    sid VARCHAR(20),
    score INT
)
""")

# 2. 插入
cursor.execute("INSERT INTO students (name, sid, score) VALUES (%s, %s, %s)", ("张三", "2023001", 85))

# 3. 查询
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()
print(results)

# 4. 提交
conn.commit()

cursor.close()
conn.close()