#!/usr/bin/python3
"""Connect to mysql DB from python"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3906, user=user_name,
                        passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities LEFT JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
