#!/usr/bin/python3
""" This script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa.
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    cities = ""
    sql = """SELECT cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id;"""
    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute(sql)
    states = cur.fetchall()
    for i in states:
        if i[1] == argv[4]:
            if cities != "":
                cities += ", "
            cities += i[0]
    print(cities)
