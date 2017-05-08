import requests
import re
import sqlite3

conn = sqlite3.connect('kseries.db')

c = conn.cursor()

web_response = requests.get('http://www.kseries.co/rebel-hong-gil-dong/')
text_result = web_response.text

matches = re.findall('http:\/\/www.kseries.co\/clip\/(\d+)\/\"\starget=\"_blank\">(\S+)<\/a>', text_result)

for match in matches:
  c.execute("INSERT INTO links (name, id) VALUES (?, ?)", (match[1], match[0]))

conn.commit()
