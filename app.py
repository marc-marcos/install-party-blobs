from flask import Flask
import sqlite3
from flask import g

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()

    return users

@app.route("/create/<username>")
def create_user(username):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO users (Name) VALUES ('{username}')")
    conn.commit()
    conn.close()

    return {"code": 200}

@app.route("/deletedatabase")
def delete_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM users")
    conn.commit()
    conn.close()

    return {"code": 200}