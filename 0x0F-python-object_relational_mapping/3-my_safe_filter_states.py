#!/usr/bin/python3
"""displays all states of hbtn_0e_0_usa where name matches the argument."""
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
ORDER BY id
"""
    cursor.execute(query)
    for state in cursor.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
