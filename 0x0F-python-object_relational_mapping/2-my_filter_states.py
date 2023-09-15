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
WHERE BINARY name = '{}'
ORDER BY id
""".format(sys.argv[4])
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
