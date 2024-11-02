import sqlite3

def initialize_database(db_name="drift_reports.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DriftReport (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dependency TEXT NOT NULL,
        current_version TEXT,
        expected_version TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def save_drift_report(drift):
    # Call initialize_database to ensure table creation
    initialize_database()
    conn = sqlite3.connect('drift_reports.db')
    cursor = conn.cursor()
    for dependency, versions in drift.items():
        cursor.execute("INSERT INTO DriftReport (dependency, current_version, expected_version) VALUES (?, ?, ?)",
                       (dependency, versions['current'], versions['expected']))
    conn.commit()
    conn.close()
