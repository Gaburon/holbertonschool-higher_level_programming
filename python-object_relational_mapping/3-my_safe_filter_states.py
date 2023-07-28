#!/usr/bin/python3
""" This script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument. But this time,
    write one that is safe from MySQL injections!
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()
    for i in states:
        if i[1] == argv[4]:
            print("{}".format(i))
    cur.close
