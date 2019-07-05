import Adafruit_DHT
import time
import sqlite3
from datetime import datetime
import random

def open_db():
  conn = sqlite3.connect("sensordata.db")
  print("Connected to database sucessfully...")
  return conn

def close_DB(conn):
  conn.close()

def get_time():
  now = datetime.now()
  curr_time = now.strftime("%M:%S")
  return curr_time

def insert(temp, hum, timest, idd):
  sql = "INSERT INTO 'sensorTable' ('id', 'Temperature', 'Humidity', 'Timestamp') VALUES ('" + str(idd) + "','" + str(temp) + "','" + str(hum) + "','" + str(timest) + "')"
  print (sql)
  print("INS: ", cur.execute(sql).rowcount)
  conn.commit()

def rm():
  sql = "DELETE FROM sensorTable WHERE CAST(id AS INTEGER) = (SELECT min(CAST(id AS INTEGER)) FROM sensorTable)" 
  rv = cur.execute(sql).rowcount
  print("rv: ", rv)
  conn.commit()

conn = open_db()
cur = conn.cursor()

sql = "SELECT count(*) FROM sensorTable"
cur.execute(sql)
count = cur.fetchone()[0]
print ("first count: ", count)

sensor = Adafruit_DHT.DHT11

# Set GPIO sensor is connected to
gpio = 14

try:
  while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

    if (humidity is not None) and (temperature is not None):
      count += 1
      print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
      print("Time: " + str(get_time()))
      print("Id: ", count)
      insert(temperature, humidity, str(get_time()), count)

      if count >= 5:
        rm()
        print("after insert counter:", count)
    else:
      print('Failed to get reading. Try again!')
    
    time.sleep(5)

except KeyboardInterrupt:
  cur.close()
  conn.close()
  exit()
