import re
regex = re.compile(r'^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$', re.IGNORECASE)

email = input("www.alierbey.com: ") 

if not re.match(regex, email):
  print("URL geçersiz")
else:
  print("URL geçerli")
