from flask import Flask, request, jsonify
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

@app.route("/create", methods=['POST'])
def create_user():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        # Use parameterized query to prevent SQL injection
        c.execute("INSERT INTO users (Name, Os) VALUES (?, ?)", (request.form['username'], request.form['os']))
        conn.commit()
    except sqlite3.Error as e:
        # Return an error message if something goes wrong
        return jsonify({"code": 500, "message": str(e)})
    finally:
        # Ensure the connection is closed
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