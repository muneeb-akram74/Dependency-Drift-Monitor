import sqlite3

def create_drift_table(db_name="drift_reports.db"):
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

def save_drift_report(drift_data, db_name="drift_reports.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for dep, versions in drift_data.items():
        cursor.execute("INSERT INTO DriftReport (dependency, current_version, expected_version) VALUES (?, ?, ?)",
                       (dep, versions["current"], versions["expected"]))
    conn.commit()
    conn.close()
