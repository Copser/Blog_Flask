# sql.py - Create a SQLite3 databse and populate it whit data
import sqlite3

# create a new databse if the databse doesn't already exist
with sqlite3.connect("blog.db") as connection:
    # get a cursor object used to execute SQL commands
    c = connection.cursor()
    # create the table
    c.execute("""
        CREATE TABLE posts(title TEXT, post TEXT)
        """)

    # insert dumy data into the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')
