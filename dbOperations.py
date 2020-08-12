import sqlite3

def createConnection(func):

    def wrapper(*args):
        global conn, curr
        conn = sqlite3.connect("file.db")
        curr = conn.cursor()
        input = [ arg for arg in args ]
        if len(input) == 6:
            func(*args)
        else:
            func()

        conn.commit()
        conn.close()

    return wrapper


@createConnection
def createTable():
    curr.execute("CREATE TABLE IF NOT EXISTS filedata (id INTEGER,"
                "username TEXT, eventname TEXT, eventtype TEXT,"
                "eventsource TEXT, eventtime TEXT)")

@createConnection
def truncateTable():
    curr.execute("DELETE FROM filedata")

@createConnection
def insertData(id,uname,ename,etype,esource,etime):
     curr.execute("INSERT INTO filedata VALUES(?,?,?,?,?,?)",(id,uname,ename, etype,esource,etime))


@createConnection
def queryData():
    data = curr.execute("SELECT * FROM filedata").fetchall()
    for d in data:
        print(d)

createTable()
truncateTable()
insertData(1,"VK","fncall","autodata","program","12Aug")
insertData(2,"Happy","callingFunc","autodata","Pyprogram","12Aug")
queryData()

