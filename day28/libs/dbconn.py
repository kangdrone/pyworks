import sqlite3


def getconn():
    conn = sqlite3.connect("C:/webdb/webdb.db")
    return conn