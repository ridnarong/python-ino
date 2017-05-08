import sqlite3

conn = sqlite3.connect('kseries.db')

c = conn.cursor()
c.execute('CREATE TABLE links (name text, id int, status text)')
c.execute("INSERT INTO links VALUES ('ep0', 12345, 'New')")
conn.commit()

c.execute('SELECT * FROM links WHERE name = 'abc'')
print(c.fetchone())

c.execute("INSERT INTO links VALUES (?, ?, ?)", ('ep00', 81281, 'New'))
conn.commit()

for item in c.execute('SELECT * FROM links'):
   print(item)

# Table Design
# *Series*
# field       | datatype
# -----------------------
# title       | text
# description | text
# url         | text

# *Links*
# field     | datatype
# ------------------
# id        | int
# ep        | text
# link      | text
# status    | text
# is_backup | boolean

# *Resolution*
# field       | datatype
# -----------------------
# resolution  | int