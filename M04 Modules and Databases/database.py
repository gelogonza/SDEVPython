import sqlite3

# Define the path for your database file
database_path = 'C:/Users/angel/Coding/Python/PythonSDEV/M04 Modules and Databases/books.db'

# Connect to the database (this will create the database file if it does not exist)
conn = sqlite3.connect(database_path)

# Create a cursor object
cursor = conn.cursor()

# SQL command to create the books table
create_table_sql = '''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER
);
'''

# Execute the SQL command
cursor.execute(create_table_sql)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and table initialized successfully.")
