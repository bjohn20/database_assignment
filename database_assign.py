
import sqlite3

# Created and connected to database
conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    # Created table within database and created ID and a field
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        files TEXT \
        )")
    # Saved the changes
    conn.commit()
# Closed out the program
conn.close()

conn = sqlite3.connect('test2.db')

# Tuple
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# looping through each index in tuple to find the files ending with txt
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            # each row value will be the name of the file in the tuple inserted
            # into the table
            cur.execute("INSERT INTO tbl_files(files) VALUES (?)", (x,))
            print(x)
conn.close()
