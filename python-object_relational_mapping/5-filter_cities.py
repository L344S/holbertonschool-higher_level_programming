#!/usr/bin/python3
"""Task: List all cities of a state"""
import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = connect.cursor()
    cur.execute(f"SELECT c.name \
        FROM cities AS c \
        JOIN states AS s \
            ON c.state_id = s.id \
        WHERE s.name = '{sys.argv[4].split(";")[0].strip("'")}' \
        ORDER BY c.id")
    qrows = cur.fetchall()

    idx = 0
    for row in qrows:
        if idx > 0:
            print(", ", end="")
        print(row[0], end="")
        idx += 1
    print()
