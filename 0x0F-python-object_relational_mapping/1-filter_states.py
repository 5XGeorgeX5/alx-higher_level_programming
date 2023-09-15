#!/usr/bin/python3
"""lists all states with a name starting with N from hbtn_0e_0_usa"""
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
SELECT *
FROM states
WHERE BINARY name LIKE 'N%'
ORDER BY id
"""
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
