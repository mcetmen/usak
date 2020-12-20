print("3 basamaklı rakanları birbirinden olan sayılar:")
sayac=0
for i in range (100,999):
 a = int(i/100);
 b = int((i%100)/10);
 c = i%10;
 if a!=b and a!=c and b!=c:
   print(i)
   sayac=sayac+1

print("3 basamaklı rakanları birbirinden olan sayıların toplamı:",sayac)
