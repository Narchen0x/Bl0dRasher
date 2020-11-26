import sqlite3
import os
from io import open

class database:
    def test():
        ruta = "Resources/database.db"
        global cursor, connect
        connect = sqlite3.connect(ruta)
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER(255) NOT NULL UNIQUE,
            user VARCHAR(255)
        );""")
        connect.commit()
        print("Database run correctly.")
    test()

    # Register user
    def register(user_id, username):
        cursor.execute(f'INSERT INTO users VALUES (null, "{user_id}", "{username}");')
        connect.commit()
        print(f"New user: {username}")
    
    def check(user_id):
        cursor.execute(f'SELECT user_id FROM users WHERE user_id = "{user_id}"')
        check = cursor.fetchall()
        connect.commit()
        try:
            for l in check:
                for element in l:
                    user = element
            if int(user) == int(user_id):
                return True
        except:
            return False

    # Show values on database
    def show():
        archivo = open("Resources/user_data.txt", "w+")
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        table = ""
        for user in users:
            table += f"User: {user[0]}\nID: {user[1]}\nUsername: {user[2]}\n\n"
        archivo.write(table)
        return table

    def delete(user_id):
        cursor.execute(f"SELECT user_id FROM users WHERE user_id = {user_id}")
        userd = cursor.fetchall()
        for x in userd:
            for y in x:
                userid = y
        if int(userid) == int(user_id):
            cursor.execute(f"SELECT user FROM users WHERE user_id = {user_id}")
            usernl = cursor.fetchall()
            for x in usernl:
                for y in x:
                    username = y
            cursor.execute(f'DELETE FROM users WHERE user_id = "{user_id}"')
            connect.commit()
            return username
        #cursor.execute(f'DELETE FROM usuarios WHERE user_id = "{user_id}"')

    def delete_file():
        os.remove("Resources/user_data.txt")
