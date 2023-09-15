#!/usr/bin/python3
"""lists all states with a name starting with N from hbtn_0e_0_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
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
