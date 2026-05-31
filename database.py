import sqlite3

def create_table():
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        dob TEXT,
        email TEXT,
        glucose REAL,
        haemoglobin REAL,
        cholesterol REAL,
        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_patient(name, dob, email, glucose, haemoglobin, cholesterol, remarks):
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (name, dob, email, glucose, haemoglobin, cholesterol, remarks)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (name, dob, email, glucose, haemoglobin, cholesterol, remarks))

    conn.commit()
    conn.close()


def view_patients():
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")
    data = cursor.fetchall()

    conn.close()
    return data


def update_remarks(patient_id, new_remarks):
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE patients SET remarks=? WHERE id=?",
        (new_remarks, patient_id)
    )

    conn.commit()
    conn.close()


def delete_patient(patient_id):
    conn = sqlite3.connect("health.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id=?",
        (patient_id,)
    )

    conn.commit()
    conn.close()