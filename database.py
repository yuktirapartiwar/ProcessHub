import sqlite3
from pathlib import Path

DB_PATH = Path("data/workflow_tracker.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT NOT NULL,

        process_type TEXT NOT NULL,

        created_date TEXT NOT NULL,

        completed_date TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
                   
        resource_id INTEGER NOT NULL,
                   
        process_name TEXT NOT NULL,

        task_name TEXT NOT NULL,
        
        task_type TEXT NOT NULL,
        
        status TEXT NOT NULL,
                   
        remarks TEXT,
                   
        Foreign Key (resource_id) 
        REFERENCES resources(id)
    )               
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS task_dependencies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        
        task_id INTEGER NOT NULL,
        
        depends_on_task_id INTEGER NOT NULL,
        
        Foreign Key (task_id) 
        REFERENCES tasks(id),
        
        Foreign Key (depends_on_task_id) 
        REFERENCES tasks(id)
    )
    """)

    conn.commit()
    conn.close()