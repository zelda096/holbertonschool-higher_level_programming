#!/usr/bin/python3
"""
lists all states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s\
    ORDER BY states.id ASC", (argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
