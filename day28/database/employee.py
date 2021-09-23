# employee 테이블 관리
from day28.libs.dbconn import getconn
import sqlite3

# 전체 자료 검색
def select_data():
    #conn = sqlite3.connect("C:/webdb/webdb.db")
    conn = getconn()
    cur = conn.cursor()   #cur는 모든 작업을 하는 객체
    sql = "SELECT * FROM employee ORDER BY salary DESC"
    cur.execute(sql)  # db에서 sql문을 실행
    rs = cur.fetchall()  # db에서 가져온 모든 자료 리스트로 기억(ResultSet)
    for i in rs:
        print(i)
    conn.close()

# 자료 추가
def insert_data():
    #conn = sqlite3.connect("C:/webdb/webdb.db")
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO employee VALUES ('e20001', '흥부', 31, 1000)"
    cur.execute(sql)
    # sql = "INSERT INTO employee VALUES (?, ?, ?, ?)"
    # cur.execute(sql, ('e1005', '박인비', 33, 15000)) # 동적 바인딩 방식
    conn.commit()    # 삽입, 수정, 삭제시는 반드시 명시해야 함
    conn.close()

# 자료 수정
def update_data():
    #conn = sqlite3.connect("C:/webdb/webdb.db")
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE employee SET age = ?, salary = ? WHERE emp_id = ?"
    cur.execute(sql, (20, 5000, 'e1004'))
    conn.commit()
    conn.close()

# 자료 삭제
def delete_data():
    #conn = sqlite3.connect("C:/webdb/webdb.db")
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE emp_id = ?"
    cur.execute(sql, ('e1003', ))  # 튜플은 1개 추가할때 뒤에 콤머 붙인 : 주의!!
    conn.commit()
    conn.close()

# 자료 1개 검색
def select_one():
    #conn = sqlite3.connect("C:/webdb/webdb.db")
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM employee WHERE emp_id = ?"
    cur.execute(sql, ('e1002', ))
    rs = cur.fetchone()  # 1개를 가져와서 기억
    print(rs)
    conn.close()

if __name__ == "__main__":
    # delete_data()
    # update_data()
    # insert_data()
    select_data()
    # select_one()