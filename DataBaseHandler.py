#db imports
import sqlite3                      #
from dataclasses import dataclass   #
from typing import Optional         #

class DataBaseEvents():

    def __init__(self, db_name = "MyDB.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.createtable()

    def createtable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS locations (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            country TEXT,
                            province TEXT,
                            locality TEXT,
                            district TEXT,
                            latitude TEXT,
                            longtitude TEXT
                            )
        ''')
        self.conn.commit()
    
    def insertiteration(self, ):
        print("ok")
            