import sqlite3 # Import the sqlite3 
db = sqlite3.connect("contact.sqlite") # Create Connection 
cursor = db.cursor() # Create Cursor object
# Create a string to hold the SQL query
sql="""
    CREATE TABLE IF NOT EXISTS contacts (
    contact_id integer PRIMARY KEY,
    first_name text,
    last_name text,
    email text,
    phone text); """
cursor.execute(sql) # Pass the string
db.commit() # Save change permanently


sql="""
    INSERT INTO contacts (contact_id, first_name, last_name, email, phone)
    VALUES (1100, 'hi', 'Ok', 'bj@number10.com', 'Fun');
"""
cursor.execute(sql) # Pass the string variable
db.commit() # Save permanently

sql= "Select * from contacts"
cursor.execute(sql)
print(cursor.fetchall())