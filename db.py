import sqlite3

from flask import current_app, g

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(error=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf-8"))

def init_app(app):
    app.teardown_appcontext(close_db) #when a request ends, call close.db

    @app.cli.command("init-db") #creates new terminal command
    def init_db_command():
        init_db()
        print("Database initialised")