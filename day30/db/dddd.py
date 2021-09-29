import sqlite3

def getconn():
    conn = sqlite3.connect("c:/")
    return conn

def insert():
    conn = getconn()
    cur = conn.curser()
    sql = " INSERT INTO member(age, age ,age) VALUES (?, ?, ?)"