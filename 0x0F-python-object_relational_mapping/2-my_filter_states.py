#!/usr/bin/python3
"""displays all states of hbtn_0e_0_usa where name matches the argument."""
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
WHERE BINARY name = '{}'
ORDER BY id
""".format(argv[4])
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
