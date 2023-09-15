#!/usr/bin/python3
"""lists all cities of that state, using the database hbtn_0e_4_usa"""
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
    c.name,
    s.name
FROM cities c
JOIN states s
    ON c.state_id = s.id
ORDER BY c.id
"""
    cursor.execute(query)
    cities = [city[0] for city in cursor.fetchall() if city[1] == sys.argv[4]]
    print(", ".join(cities))
