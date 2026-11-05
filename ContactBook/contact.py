import sqlite3
import os

DATABASE = "database/contacts.db"


# Create Database and Table
def initialize_database():

    os.makedirs("database", exist_ok=True)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    """)

    conn.commit()
    conn.close()


# 1. Add Contact
def add_contact(name, phone, email):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO contacts (name, phone, email)
        VALUES (?, ?, ?)
    """, (name, phone, email))

    conn.commit()
    conn.close()


# 2. View All Contacts
def get_contacts():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM contacts
        ORDER BY id DESC
    """)

    contacts = cursor.fetchall()

    conn.close()

    return contacts


# 3. Search Contacts
def search_contacts(search_name):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM contacts
        WHERE name LIKE ?
        ORDER BY name
    """, ('%' + search_name + '%',))

    contacts = cursor.fetchall()

    conn.close()

    return contacts


# 4. Delete Contact
def delete_contact(contact_id):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM contacts
        WHERE id = ?
    """, (contact_id,))

    conn.commit()
    conn.close()
