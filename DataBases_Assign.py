import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Create a connection to the database (or create the database if it doesn't exist)
conn = sqlite3.connect('fileList.db')

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Create a table to store the file names (if it doesn't already exist)
cur.execute('CREATE TABLE IF NOT EXISTS fileNames (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')

# Loop through the list of file names and add any .txt files to the database
for fileName in fileList:
    if fileName.endswith('.txt'):
        cur.execute('INSERT INTO fileNames (name) VALUES (?)', (fileName,))
        print(f'Added {fileName} to the database')

# Commit changes and close the database connection
conn.commit()
conn.close()

# Reconnect to the database and print the list of qualifying file names
conn = sqlite3.connect('fileList.db')
cur = conn.cursor()
cur.execute('SELECT * FROM fileNames WHERE name LIKE "%.txt"')
rows = cur.fetchall()

print('\nQualifying file names:')
for row in rows:
    print(row[1])

# Close the database connection
conn.close()
