import sqlite3

def createConnection(func):

    def wrapper(*args):
        global conn, curr
        conn = sqlite3.connect("data.db")
        curr = conn.cursor()
        input = [ arg for arg in args ]
        if len(input) == 5:
            func(*args)
        else:
            fn = func()
            conn.commit()
            conn.close()
            return fn

        conn.commit()
        conn.close()

    return wrapper


@createConnection
def createTable():
    curr.execute("CREATE TABLE IF NOT EXISTS inputdata (username TEXT, "
                 "eventname TEXT, eventtype TEXT,"
                "eventsource TEXT, eventtime TEXT)")

@createConnection
def truncateTable():
    curr.execute("DELETE FROM inputdata")

@createConnection
def insertData(uname,ename,etype,esource,etime):
     curr.execute("INSERT INTO inputdata VALUES(?,?,?,?,?)",(uname,ename, etype,esource,etime))


@createConnection
def queryData():
    data = curr.execute("SELECT * FROM inputdata").fetchall()
    return data

# createTable()
# truncateTable()
# insertData(1,"VK","fncall","autodata","program","12Aug")
# insertData(2,"Happy","callingFunc","autodata","Pyprogram","12Aug")
# d = queryData()
# print(d)
