#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = database.cursor()
    query = """
SELECT
    c.id,
    c.name,
    s.name
FROM cities c
JOIN states s
    ON c.state_id = s.id
ORDER BY c.id
"""
    cursor.execute(query)
    for city in cursor.fetchall():
        print(city)
