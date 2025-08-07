"""
CIS2532
HW12
Author: <NAME>
This program follows along with the example in section 17.2 of the Intro to Python
For Computer Science book
"""

import sqlite3
import pandas as pd

#connect to database
connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10

#view author table contents
print(pd.read_sql("SELECT * FROM authors", connection, index_col='id'))
#titles table
print(pd.read_sql("SELECT * FROM titles", connection))
#author/ISBN table with foreign keys
df = pd.read_sql("SELECT * FROM author_ISBN", connection)
print(df.head())

#select queries
print(pd.read_sql("SELECT first, last FROM authors", connection))

#where clause - must be single qotes for str comparison
print(pd.read_sql("SELECT title, edition, copyright FROM titles WHERE copyright > '2016'", connection))
#like - pattern matching
print(pd.read_sql("SELECT id, first, last FROM authors WHERE last LIKE 'D%'", connection, index_col='id'))
#any character
print(pd.read_sql("SELECT id, first, last FROM authors WHERE first LIKE '_b%'", connection, index_col='id'))

#order by clause
print(pd.read_sql("SELECT title FROM titles ORDER BY title ASC", connection))
#sort by multiple columns
print(pd.read_sql("SELECT id, first, last FROM authors ORDER BY last, first", connection, index_col='id'))
print(pd.read_sql("SELECT id, first, last FROM authors ORDER BY last DESC, first ASC", connection, index_col='id'))

#combine where and order
print(pd.read_sql("SELECT isbn, title, edition, copyright FROM titles WHERE title LIKE '%How to Program' ORDER BY title", connection))

#merging data
print(pd.read_sql("SELECT first, last, isbn FROM authors INNER JOIN author_ISBN ON authors.id = author_ISBN.id ORDER BY last, first", connection).head())

#insert
cursor = connection.cursor()
cursor = cursor.execute("INSERT INTO authors (first, last) VALUES ('Sue', 'Red')")
print(pd.read_sql("SELECT id, first, last FROM authors", connection, index_col='id'))

#update
cursor = cursor.execute("UPDATE authors SET last='Black' WHERE last='Red' AND first='Sue'")
print(cursor.rowcount) #confirm update
print(pd.read_sql("SELECT id, first, last FROM authors", connection, index_col='id'))

#delete
cursor = cursor.execute("DELETE FROM authors WHERE id='6'")
print(cursor.rowcount)
print(pd.read_sql("SELECT id, first, last FROM authors", connection, index_col='id'))


#self-check exercises
#select titles
print(pd.read_sql("SELECT title, edition FROM titles ORDER BY edition DESC", connection).head(3)) #show first three

#A name authors
print(pd.read_sql("SELECT * FROM authors WHERE first LIKE 'A%'", connection))

#NOT keyword
print(pd.read_sql("SELECT isbn, title, edition, copyright FROM titles WHERE title NOT LIKE '%How to Program' ORDER BY title", connection))
