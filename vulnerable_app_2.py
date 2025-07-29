import sqlite3
import os
sonar.python.version


def connect_db():
    return sqlite3.connect("users.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)')
    conn.commit()
    conn.close()

def insert_user(username):
    conn = connect_db()
    cursor = conn.cursor()

   
    query = f"INSERT INTO users (username) VALUES ('{username}')"
    cursor.execute(query)
    conn.commit()
    conn.close()

def list_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def dangerous_eval():
  
    user_input = input("Enter Python code to eval: ")
    eval(user_input) 

def insecure_os_call():

    filename = input("Enter filename to list: ")
    os.system(f"ls {filename}")  

if __name__ == "__main__":
    create_table()
    insert_user("admin'); DROP TABLE users; --")  
    list_users()
