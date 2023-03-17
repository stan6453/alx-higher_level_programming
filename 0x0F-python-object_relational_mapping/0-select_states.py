#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import MySQLdb

    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3906, user=user_name,
                        passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
