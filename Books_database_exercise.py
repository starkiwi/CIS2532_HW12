"""
CIS2532
HW12
Author: Kieran Reid
This program explores a book database as an example of how to deal with big data
"""
import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10

#select authors' last names in descending order
print(pd.read_sql("SELECT last FROM authors ORDER BY last DESC", connection))
print()

#select book titles in ascending order
print(pd.read_sql("SELECT title FROM titles ORDER BY title ASC", connection))
print()

#use INNER JOIN to select all books for a specific author
print(pd.read_sql("SELECT title, copyright, titles.isbn FROM titles INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn INNER JOIN authors ON authors.id = author_ISBN.id WHERE first = 'Harvey' ORDER BY title", connection))
print()

#insert new author
cursor = connection.cursor()
cursor.execute("INSERT INTO authors (first, last) VALUES ('Osamu', 'Dazai')")
new_id = cursor.lastrowid
print(pd.read_sql("SELECT first, last FROM authors", connection))
print()

#insert a new title for an author
cursor.execute("INSERT INTO author_ISBN (id, isbn) VALUES (?, '9780811204811')", (new_id,))
cursor.execute("INSERT INTO titles (isbn, title, edition, copyright) VALUES ('9780811204811', 'No Longer Human', 8, '1973')")
print(pd.read_sql("SELECT isbn, title, edition, copyright FROM titles ORDER BY title ASC", connection))

