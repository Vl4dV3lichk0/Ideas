import sqlite3

def connect():
    # Create database
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    # Create table Categories
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
    );
    ''')

    # Create table Ideas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ideas (
    id INTEGER PRIMARY_KEY,
    name TEXT NOT NULL,
    about TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    is_done BOOLEAN NOT NULL,
    priority INTEGER NOT NULL,
    creation_date DATE,
    CONSTRAINT fk_category_id FOREIGN KEY (category_id) REFERENCES Categories (id) 
    );
    ''')

    # Save and exit
    connection.commit()
    connection.close()