import sqlite3

# 1. Izveido datu bāzi un jāpieslēdzas tai
conn=sqlite3.connect("piemers.db")
cursor=conn.cursor()

# 2. Izvediot tabulu
cursor.execute('''
               CREATE TABLE IF NOT EXISTS lietotaji(
                   id INTEGER PRIMARY KEY,
                   vards TEXT NOT NULL,
                   uzvards TEXT NOT NULL,
                   epasts TEXT NOT NULL UNIQUE 
               )
               ''')











conn.commit()
conn.close()