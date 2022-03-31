

import sqlite3

connection = sqlite3.connect('movie.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS MOVIE")
TABLE="""CREATE TABLE MOVIE(
       NAME VARCHAR(255) NOT NULL,
       ACTOR CHAR(25) NOT NULL,
       ACTRESS CHAR(25) NOT NULL,
       DIRECTOR CHAR(25) NOT NULL,
       YEAR OF RELEASE INT
       )"""
cursor.execute(TABLE)

cursor.execute('''INSERT INTO MOVIE VALUES ('Iron Man', 'Robert Downey Jr', 'Gwyneth Paltrow', 'Jon Favreau', '2008')''')
cursor.execute('''INSERT INTO MOVIE VALUES ('Thor', 'Chris Hemsworth', 'Natalie Portman', 'Kenneth Branagh', '2011')''')
cursor.execute('''INSERT INTO MOVIE VALUES ('Ant-Man', 'Paul Rudd', 'Evangeline Lilly', 'Peyton Reed', '2015')''')
cursor.execute('''INSERT INTO MOVIE VALUES ('Doctor Strange', 'Benedict Cumberbatch', 'Rachel Mcadams', 'Scott Derrickson', '2016')''')
cursor.execute('''INSERT INTO MOVIE VALUES ('Spider-Man', 'Tom Holland', 'Zendaya', 'Jon Watts', '2017')''')
print("DATA INSERTED IN THE TABLE")
connection.commit()
connection.close()
# PROGRAM TO ISSUE SELECT STATEMENT TO QUERY ALL ROWS FROM MOVIE TABLE
import sqlite3

connection = sqlite3.connect('movie.db')
cursor = connection.cursor()
statement = '''SELECT * FROM MOVIE'''
cursor.execute(statement)
print("ALL THE DATA")
output = cursor.fetchall()
for row in output:
    print(row)
    connection.close()








