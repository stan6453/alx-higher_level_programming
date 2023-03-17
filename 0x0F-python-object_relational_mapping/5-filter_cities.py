#!/usr/bin/python3
"""Connect to mysql DB from python"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user_name,
                           passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute(f"SELECT name FROM cities\
            WHERE state_id = (SELECT id from states\
                            WHERE name = %s)\
            ORDER BY id", (state,))

    query_rows = cur.fetchall()
    result = ''
    for row in query_rows:
        result += row[0] + ', '
    result = result[:-2]
    print(result)
    cur.close()
    conn.close()
