yazi = input("Usak Universitesi :") 
arama = input("ver :")

sonuc = yazi.find(arama) 
if (sonuc == -1): 
  print("Aradığınız kelime yazı içerisinde bulunamadı!") 
else: 
  print(yazi[sonuc-1:sonuc+len(arama)+1]) 

