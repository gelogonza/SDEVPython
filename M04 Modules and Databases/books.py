from sqlalchemy import create_engine, MetaData, select

# Define the path to your SQLite database
database_path = 'sqlite:///C:/Users/angel/Coding/Python/PythonSDEV/M04 Modules and Databases/books.db'

# Create an engine to connect to the SQLite database
engine = create_engine(database_path)

# Initialize MetaData
metadata = MetaData()

# Reflect the existing database into the new model
metadata.reflect(bind=engine)

# Reference to the books table
books_table = metadata.tables['books']

# Updated: Create a SELECT query
query = select(books_table.c.title).order_by(books_table.c.title)

# Execute the query and print the titles
with engine.connect() as connection:
    result = connection.execute(query)
    for row in result:
        print(row[0])
