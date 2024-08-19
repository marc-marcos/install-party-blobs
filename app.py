from flask import Flask, request, jsonify
from flaskcors import CORS
import sqlite3
from flask import g
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()

    return users

@app.route("/create", methods=['POST'])
def create_user():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        if request.form['username'] == "": 
            c.execute("SELECT COUNT(*) FROM users")
            count = c.fetchone()[0]

            username = str(count)

        else:
            username = request.form['username']

        c.execute("INSERT INTO users (Name, Os) VALUES (?, ?)", (username, request.form['os']))
        conn.commit()
    except sqlite3.Error as e:
        return jsonify({"code": 500, "message": str(e)})
    finally:
        conn.close()

    return jsonify({"code": 200, "message": "User created successfully"})

@app.route("/deletedatabase")
def delete_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM users")
    conn.commit()
    conn.close()

    return {"code": 200}
