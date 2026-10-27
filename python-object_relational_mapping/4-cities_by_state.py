#!/usr/bin/python3
"""filter states by user input"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cur = db.cursor()
    cur.execute(
        """
        SELECT id, name
        FROM cities
        ORDER BY id;
        """,)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
