from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
from flask import g
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def main_page():
    return render_template("index.html") 

@app.route('/raw')
def raw_data():
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

        data = request.json

        if data['username'] == "": 
            c.execute("SELECT COUNT(*) FROM users")
            count = c.fetchone()[0]

            username = str(count)

        else:
            username = data['username']

        c.execute("INSERT INTO users (Name, Os) VALUES (?, ?)", (username, data['os']))
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
