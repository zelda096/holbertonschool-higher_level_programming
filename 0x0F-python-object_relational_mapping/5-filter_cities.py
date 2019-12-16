#!/usr/bin/python3
"""
takes in the name of a state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4], ))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[1])
    print(', '.join(cities))
    cur.close()
    db.close()
