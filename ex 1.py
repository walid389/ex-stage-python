
import sqlite3

conn = sqlite3.connect("ma_base_de_donnees.db")

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);")
cursor.execute("INSERT INTO users (name) VALUES ('walid');")
conn.commit()

cursor.execute("SELECT * FROM users;")
for row in cursor.fetchall():
    print(row)
#close db
cursor.close()
conn.close()

