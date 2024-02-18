#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
0-select_states.py:
script that lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE `name` LIKE\
                 'N%' ORDER BY `id` ASC "
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
