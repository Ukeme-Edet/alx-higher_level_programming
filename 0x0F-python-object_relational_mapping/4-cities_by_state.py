#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa.
"""


def main():
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8",
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN\
        states ON states.id = cities.state_id ORDER BY cities.id ASC"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
