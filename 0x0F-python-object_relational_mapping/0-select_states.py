#!/usr/bin/python3


def main(username, password, dbname):
    import MySQLdb
    port = 3306
    conn = MySQLdb.connect(
        host="localhost",
        port=port,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)


if __name__ == "__main__":
    import sys
    args = sys.argv
    mysql_username = args[0]
    mysql_password = args[1]
    database_name = args[2]
    main(mysql_username, mysql_password, database_name)
