import sqlite3

connect = sqlite3.connect('database.db')

sql = connect.cursor()


sql.execute('CREATE TABLE IF NOT EXISTS beaches (name TEXT, number INTEGER);')
connect.commit()
sql.execute('INSERT INTO beaches (name , number) VALUES ("PASHA", 909990123);')
connect.commit()
