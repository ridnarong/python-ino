import sqlite3

conn = sqlite3.connect('kseries.db')

c = conn.cursor()
c.execute('CREATE TABLE links (name text, id int, status text)')
c.execute("INSERT INTO links VALUES ('ep0', 12345, 'New')")
conn.commit()

c.execute('SELECT * FROM links')
print(c.fetchone())

c.execute("INSERT INTO links VALUES (?, ?, ?)", ('ep00', 81281, 'New'))
conn.commit()

for item in c.execute('SELECT * FROM links'):
   print(item)