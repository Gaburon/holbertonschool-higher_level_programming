#!/usr/bin/python3
""" This script that lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    sql = """SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id;"""
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute(sql)
    states = cur.fetchall()
    for i in states:
        print(i)
