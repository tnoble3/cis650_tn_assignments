import sqlite3
DB_FILE = "music.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Album (
    albumID INTEGER PRIMARY KEY AUTOINCREMENT,
    albumTitle TEXT NOT NULL,
    artistName TEXT NOT NULL,
    recordLabel TEXT NOT NULL,  
    totalDuration TEXT NOT NULL  --HH:MM:SS
  )""")
    
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Tracks (
    trackID INTEGER PRIMARY KEY AUTOINCREMENT,
    albumID INTEGER NOT NULL,
    trackTitle TEXT NOT NULL,
    totalDuration INTEGER NOT NULL, --seconds
    FOREIGN KEY (albumID) REFERENCES Album(albumID)
  )""")
    
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
