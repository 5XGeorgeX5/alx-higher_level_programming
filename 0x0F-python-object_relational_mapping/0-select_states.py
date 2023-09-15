#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa."""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    database = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    for state in cursor.fetchall():
        print(state)
