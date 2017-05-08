import requests
import re
import sqlite3

conn = sqlite3.connect('kseries.db')

c = conn.cursor()

for item in c.execute('SELECT id FROM links'):
   print(item)
