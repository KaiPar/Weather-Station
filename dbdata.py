import sqlite3
import wethearconfig
import json

dbfile = wethearconfig.getdbfile()

def opendb(sqlite_file):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    return conn, c

def get_db_allsensordata():
    con, cur = opendb(dbfile)
    cur.execute("SELECT * FROM sensorTable")
    rows = cur.fetchall()
    idd, temp, hum, ts = [], [], [], []
    for row in rows:
        idd.append(row[0])
        temp.append(row[1])
        hum.append(row[2])
        ts.append(row[3])
    
    cur.close()
    con.close()
    
    return idd, ts, temp, hum

def get_ts(ts):
    dictlist = []
    for key, value in ts.items():
        temp = [key,value]
        dictlist.append(temp)
    
    return dictlist