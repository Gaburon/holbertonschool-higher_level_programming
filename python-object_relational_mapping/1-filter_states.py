#!/usr/bin/python3
""" This script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()
    for i in states:
        if i[1][0] == 'N':
            print(i)
    cur.close()
