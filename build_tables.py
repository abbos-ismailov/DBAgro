from psycopg2 import connect

def build():
    dbc = connect(database = "dbagro", user = "postgres", password = "1234", host="localhost", port="5432")
    db = dbc.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS users(id serial primary key, name text, login text, password text, permission INT, token text);")
    dbc.commit()
    db.execute("CREATE TABLE IF NOT EXISTS plants(id serial primary key, name text, definition text, pic_path text);")
    dbc.commit()