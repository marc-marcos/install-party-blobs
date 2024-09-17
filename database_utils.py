from flask import Flask, render_template, request, redirect, url_for
import sqlite3


def create_database():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Os TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()

