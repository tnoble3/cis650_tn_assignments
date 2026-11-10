import sqlite3
import pandas as pd
DB_FILE = "music.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

def init_db():
    conn = get_connection()

    with open("schema.sql", "r") as file:
        schema = file.read()

    conn.executescript(schema)
    conn.commit()
    conn.close()
    print("Database and tables were successfully created.")
    
def add_record(title, artist, label, duration):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
                   INSERT INTO Album(albumTitle, artistName, recordLabel, totalDuration)
                   VALUES(?, ?, ?, ?)
                   """,(title, artist, label, duration))
    conn.commit()
    conn.close()
    print("Album added to the database.")
    
def add_track(albumid, title, duration):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
                   INSERT INTO Tracks(albumID, trackTitle, totalDuration)
                   VALUES(?, ?, ?)
                   """,(albumid, title, duration))
        conn.commit()
        print("Track added to the database.")
    
    except sqlite3.IntegrityError as error:
        conn.rollback()
        print(f"Track could not be added: {error}")
    
    finally:
        conn.close()

def get_all_albums():
    conn = get_connection()
    albums = pd.read_sql_query(
        "SELECT * FROM Album", conn
    )
    conn.close()
    return albums

def get_all_tracks():
    conn = get_connection()
    tracks = pd.read_sql_query(
        "SELECT * FROM Tracks", conn
    )
    conn.close()
    return tracks
