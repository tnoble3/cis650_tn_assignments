
import sqlite3
from pathlib import Path

folder = Path(__file__).resolve().parent

connection = sqlite3.connect(
    folder / "ForeignLanguagesClub.db"
)

connection.executescript(
    (folder / "ForeignLanguagesClub.sql").read_text()
)

connection.execute(
    """
    INSERT INTO Member
    (MSUUserID, MemberName, Major, LanguageSpecialty, Gender)
    VALUES (?, ?, ?, ?, ?)
    """,
    ("arivera_demo", "John Doe",
     "Computer Science", "Spanish", "Male")
)

connection.commit()
connection.close()
