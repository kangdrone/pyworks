import sqlite3

def getconn():
    conn = sqlite3.connect("c:/webdb/mydb.db")
    return conn

def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO tbl_book(title, publisher, page) VALUES (?, ?, ?);"
    cur.execute(sql, ('점프 투 장고', '박응용', 350))
    conn.commit()
    conn.close()

def select_book():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM tbl_book"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

# insert_book()
select_book()