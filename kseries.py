import requests
import re

web_response = requests.get('http://www.kseries.co/clip/49913/')
text_result = web_response.text
matches = re.search('iframe.*src=[\'|\"](\S+)[\'|\"]', text_result)

for match in matches.groups():
  print("- %s" % (match,))
