import sqlite3 as sq

def connector():
    con = sq.connect('test.db')
    return con


def fun(con):
    try:
        #con = sq.connect("test.db")
        #print("connected")
        cur = con.cursor()
    #qry="CREATE TABLE Student(name TEXT, id INT);"
    #qry = "insert into Student values('xyz',123);"
        qry = "select * from Student;"
        cur.execute(qry)
        rows = cur.fetchall()
        print(rows)
    for i in rows:
        print(i)
    #print("table is created")
except Exception as e:
    print(e)
finally:
    con.close()