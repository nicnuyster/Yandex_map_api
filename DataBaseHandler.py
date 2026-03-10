#db imports
import sqlite3                      #
from dataclasses import dataclass   #
from typing import Optional         #
from LocationData import Location

class DataBaseEvents():

    def __init__(self, db_name = "MyDB.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.createtable()

    def createtable(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS locations (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            address TEXT,
                            country TEXT,
                            province TEXT,
                            locality TEXT,
                            district TEXT,
                            latitude TEXT,
                            longtitude TEXT
                            )
        ''')
        self.conn.commit()
    
    def insertiteration(self, loc: Location):
        self.cursor.execute('''
            INSERT INTO locations (address, country, province, locality, district, latitude, longtitude)
            VALUES (?,?,?,?,?,?,?)
            ''', (loc.address, loc.country, loc.province, loc.locality, loc.district, loc.latitude, loc.longitude))
        self.conn.commit()
        print(self.cursor.lastrowid)
        #return self.cursor.lastrowid

    def deletetable(self, table_name):

        self.cursor.execute(f'''
            DROP TABLE IF EXISTS {table_name}
        ''')

    def close(self):
        self.clonn.close()
            