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
# field       | datatype  | Null  | Default
# -------------------------------------------
# title       | text      | No    | 
# description | text      | No    | 
# url         | text      | No    | 

# *Links*
# field     | datatype  | Null  | Default
# --------------------------------------------
# id        | int       | No    |
# ep        | text      | No    |
# link      | text      | No    |    
# status    | text      | Yes   |  'New'
# is_backup | boolean   | Yes   |  false

# *Resolution*
# field       | datatype  | Null  | Default
# --------------------------------------------
# resolution  | int       | No    |

# ตัวอย่าง การสร้าง Table
# https://www.w3schools.com/sql/sql_default.asp