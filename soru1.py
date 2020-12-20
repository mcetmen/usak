import re

email = input("ali.erbey@usak.edu.tr: ") 
regex = re.compile(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")


if not regex.match(email):
  print("Email adresi geçersiz")
else:
  print("Email adresi geçerli")

