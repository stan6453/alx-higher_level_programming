#!/usr/bin/python3
import sys
import MySQLdb

user_name = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]
state = sys.argv[4]

conn = MySQLdb.connect(host="localhost", port=3906, user=user_name,
                       passwd=password, db=db_name, charset="utf8")
cur = conn.cursor()
cur.execute(f"SELECT * FROM cities\
        WHERE cities.state_id = (SELECT id from states\
                                 WHERE name = %s)", (state,))

query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
