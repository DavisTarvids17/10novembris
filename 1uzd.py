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

# 3. Izveidot otru tabulu ar relāciju

cursor.execute('''
               CREATE TABLE IF NOT EXISTS pasutijumi(
                    id INTEGER PRIMARY KEY,
                    lietotaja_id INTEGER,
                    produkta_nosaukums TEXT NOT NULL,
                    daudzums INTEGER NOT NULL,
                    FOREIGN KEY (lietotaja_id) REFERENCES lietotaji(id)
               )
               ''')

# 4. Ievietot datus lietotāju tabulā
#cursor.execute("INSERT INTO lietotaji (vards, uzvards, epasts) VALUES (?, ?, ?)",('Jānis', 'Bērziņš', 'janis.berzins@example.lv'))
#cursor.execute("INSERT INTO lietotaji (vards, uzvards, epasts) VALUES (?, ?, ?)",('Alise', 'Liepiņa', 'alise.liepina@example.com'))
# 5. Ievietot datus pasūtījuma tabulā

cursor.execute("INSERT INTO pasutijumi (lietotaja_id, produkta_nosaukums, daudzums) VALUES (?, ?, ?)",(1, 'Dators', 2))
cursor.execute("INSERT INTO pasutijumi (lietotaja_id, produkta_nosaukums, daudzums) VALUES (?, ?, ?)",(2, 'Televizors', 5))


conn.commit()
conn.close()

