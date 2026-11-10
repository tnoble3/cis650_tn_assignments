CREATE TABLE IF NOT EXISTS Album (
    albumID INTEGER PRIMARY KEY AUTOINCREMENT,
    albumTitle TEXT NOT NULL,
    artistName TEXT NOT NULL,
    recordLabel TEXT NOT NULL,  
    totalDuration TEXT NOT NULL  --HH:MM:SS
  
);

CREATE TABLE IF NOT EXISTS Tracks (
    trackID INTEGER PRIMARY KEY AUTOINCREMENT,
    trackTitle TEXT NOT NULL,
    totalDuration INTEGER NOT NULL --seconds
    FOREIGN KEY (albumID) REFERENCES Album(albumID)
);
