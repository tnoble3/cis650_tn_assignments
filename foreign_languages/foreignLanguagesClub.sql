CREATE TABLE IF NOT EXISTS Member (
    MemberID INTEGER PRIMARY KEY AUTOINCREMENT,
    MSUUserID TEXT NOT NULL UNIQUE,
    MemberName TEXT NOT NULL,
    Major TEXT,
    LanguageSpecialty TEXT,
    Gender TEXT
);

CREATE TABLE IF NOT EXISTS Semester (
    SemesterID INTEGER PRIMARY KEY AUTOINCREMENT,
    Term TEXT NOT NULL CHECK (Term IN ('Spring', 'Summer', 'Fall', 'Winter')),
    Year INTEGER NOT NULL,
    UNIQUE (Term, Year)
);

CREATE TABLE IF NOT EXISTS Payment (
    ReceiptID INTEGER PRIMARY KEY AUTOINCREMENT,
    MemberID INTEGER NOT NULL,
    SemesterID INTEGER NOT NULL,
    PaymentDate TEXT NOT NULL DEFAULT (date('now')),
    AmountPaid NUMERIC NOT NULL DEFAULT 5.00 CHECK (AmountPaid > 0),
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
    FOREIGN KEY (SemesterID) REFERENCES Semester(SemesterID)
);

CREATE TABLE IF NOT EXISTS ClubEvent (
    EventID INTEGER PRIMARY KEY AUTOINCREMENT,
    EventDate TEXT NOT NULL,
    EventTime TEXT NOT NULL,
    Topic TEXT NOT NULL,
    Location TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Attendance (
    EventID INTEGER NOT NULL,
    MemberID INTEGER NOT NULL,
    Comments TEXT,
    NumberOfGuests INTEGER NOT NULL DEFAULT 0
        CHECK (NumberOfGuests BETWEEN 0 AND 2),
    PRIMARY KEY (EventID, MemberID),
    FOREIGN KEY (EventID) REFERENCES ClubEvent(EventID),
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
);