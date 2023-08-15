from model import User
import sqlite3

def get_db(app):
    db = getattr(app, '_database', None)
    if db is None:
        db = app._database = sqlite3.connect(app.config['DATABASE'])
        db.row_factory = sqlite3.Row
    return db

def init_db(app):
    with app.app_context():
        db = get_db(app)
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def close_db(app):
    db = getattr(app, '_database', None)
    if db is not None:
        db.close()

def insert(app, user: User):
    db = get_db(app)
    db.execute('INSERT INTO users (username, password, nome) VALUES (?, ?, ?)', (user.username, user.password, user.nome))
    db.commit()

def auth(app, user: User):
    db = get_db(app)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user.username, user.password))
    rows = cursor.fetchall()
    
    if rows:
        return User(rows[0][1], rows[0][2], rows[0][3])