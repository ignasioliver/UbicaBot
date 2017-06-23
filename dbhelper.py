# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 01:27:34 2017

@author: Ignasi Dev
"""

# Save the city and the people it has been asked
# Data will automatically be saved at the folder__pycache__

import sqlite3

class DBHelper:

    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS items (city text, people text)"
        itemidx = "CREATE INDEX IF NOT EXISTS itemIndex ON items (city ASC)"
        ownidx = "CREATE INDEX IF NOT EXISTS ownIndex ON items (people ASC)"
        self.conn.execute(tblstmt)
        self.conn.execute(itemidx)
        self.conn.execute(ownidx)
        self.conn.commit()

    def add_item(self, item_text, people):
        stmt = "INSERT INTO items (city, people) VALUES (?, ?)"
        args = (item_text, people)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text, people):
        stmt = "DELETE FROM items WHERE city = (?) AND people = (?)"
        args = (item_text, people )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self, people):
        stmt = "SELECT city FROM items WHERE people = (?)"
        args = (people, )
        return [x[0] for x in self.conn.execute(stmt, args)]
