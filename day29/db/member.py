# member 테이블 생성 및 관리
from day28.libs.dbconn import getconn
import sqlite3

def create_table():
    conn = sqlite3.connect("c:/webdb/webdb.db")  # db 연결 객체 생성
    cur = conn.cursor()  # db 작업객체 생성
    sql = """
        CREATE TABLE member(
            memberId char(5) PRIMARY kEY,
            passwd   char(8) NOT NULL,
            name     TEXT NOT NULL,
            age      INTEGER
    )
    """
    cur.execute(sql)
    conn.commit()
    conn.close()

def insert_member():
    # conn = sqlite3.connect("c:/webdb/webdb.db")  # db 연결 객체 생성
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO member(memberId, passwd, name, age) VALUES (?, ?, ?, ?)"
    cur.execute(sql, ('10002', 'b1234567', '팥쥐', 18))
    conn.commit()
    conn.close()

def select_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

# create_table()
insert_member()
select_member()