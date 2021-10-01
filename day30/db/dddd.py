import sqlite3

def getconn():
    conn = sqlite3.connect("c:/")
    return conn

def select_book():
    conn = getconn()
    cur = conn.cursor()
    sql ="SELECT * FROM book;"
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

def insert_book():
    conn = getconn()
    cur = conn.cursor()
    sql ="INSERT INTO book(age, name) VALUES (?, ?)"
    cur.execute(sql, ("장고 점프", 350))
    conn.commit()
    conn.close()


insert_book()
select_book()

