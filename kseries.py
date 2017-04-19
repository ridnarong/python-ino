import requests
import re
# โจทย์ คือ เข้าไปหา ลิงก์ ของทุก ep ใน series เรื่องนั้นทั้งหมด ตาม url ด้านล่าง 
# ลอง view source หรือ inspect element เพื่อดูโครงสร้างของหน้าเว็บเพจ
web_response = requests.get('http://www.kseries.co/rebel-hong-gil-dong/')
text_result = web_response.text
# แก้ไข regular expression โดย ศึกษาจาก http://rubular.com/ ว่าจะเอาลิงก์มาได้ยังไง
matches = re.search('iframe.*src=[\'|\"](\S+)[\'|\"]', text_result)

for match in matches.groups():
  print("- %s" % (match,))
