import sqlite3

#Подключение к базе данных
connection = sqlite3.connect('my_users.db')
#Переводчик с Python на SQL
sql = connection.cursor()

#Создание таблицы users
sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, username TEXT);')
#Добавление новых данных
sql.execute('INSERT INTO users (user_id, username) VALUES (0, "@pav_ok");')
#Вывести колонку user_id
sql.execute('SELECT user_id FROM users;')
#Запрос с фильтрацией
print(sql.execute('SELECT username FROM users WHERE user_id=0;').fetchall())
#Обновление данных
sql.execute('UPDATE users SET username="@pasha23" WHERE user_id=0;')
print(sql.execute('SELECT * FROM users;').fetchall())
#Удаление данных
sql.execute('DELETE FROM users WHERE user_id=0;')
#Фиксируем изменения
connection.commit()
