import sqlite3
import os

# [1] 하드코딩된 비밀번호 (S2068 유사 탐지 가능)
DB_PASSWORD = "supersecret123"  # 취약점: 하드코딩된 비밀번호

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

    # [2] SQL Injection 취약점
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
    # [3] 사용자 입력을 eval()에 직접 사용 (심각한 취약점)
    user_input = input("Enter Python code to eval: ")
    eval(user_input)  # ⚠️ 매우 위험

def insecure_os_call():
    # [4] 사용자 입력을 OS 명령어에 사용
    filename = input("Enter filename to list: ")
    os.system(f"ls {filename}")  # 취약점: Command Injection

if __name__ == "__main__":
    create_table()
    insert_user("admin'); DROP TABLE users; --")  # SQLi 테스트
    list_users()
    #dangerous_eval()  # 사용 시 주의
    #insecure_os_call()  # 사용 시 주의