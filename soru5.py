text1 = "receive-23-1-0\n"
text2 = "send-181-3-0-1\nreceive-170-3-0\n"
text3 = "receive-150-0-1\n0-4-5-6-2\n"
text4 = "receive-227-1-1\nsend-0-4-1-1\n"

# text = input("Lütfen ifade/ifadeleri giriniz : ")

ifadeler = text4.split("\n")
for i in range(0, len(ifadeler) - 1):
    ifade = ifadeler[i].split("-")
    if ifade[0] == "receive":
        if len(ifade) - 1 == 3:
            sinyal = int(ifade[1])
            cihaz = int(ifade[2])
            durum = int(ifade[3])
            if sinyal < 0 or sinyal > 255:
                print("Error : birinci bölüm hatalı")
            elif cihaz < 0 or cihaz > 4:
                print("Error : ikinci bölüm hatalı")
            elif durum < 0 or durum > 1:
                print("Error : üçüncü bölüm hatalı")
            else:
                print("Kod Tipi : receive - Gelen")
                if sinyal >= 0 and sinyal <= 50:
                    print("Sinyal Gucu : ", ifade[1], " - Çok Zayıf ")
                elif sinyal >= 51 and sinyal <= 100:
                    print("Sinyal Gucu : ", ifade[1], " - Zayıf Sinyal")
                elif sinyal >= 101 and sinyal <= 150:
                    print("Sinyal Gucu : ", ifade[1], " - Orta Sinyal")
                elif sinyal >= 151 and sinyal <= 200:
                    print("Sinyal Gucu : ", ifade[1], " - Güçlü Sinyal")
                elif sinyal >= 201 and sinyal <= 255:
                    print("Sinyal Gucu : ", ifade[1], " - Çok Güçlü Sinyal")
                if cihaz == 1:
                    print("Cihaz : 1 - Televizyon")
                elif cihaz == 2:
                    print("Cihaz : 2 - Camasir Makinesi")
                elif cihaz == 3:
                    print("Cihaz : 3 - Buzdolabi")
                elif cihaz == 4:
                    print("Cihaz : 4 - Firin")
                if durum == 1:
                    print("Durum : 0 - Off")
                elif durum == 2:
                    print("Durum : 1 - On")
        else:
            print("Error : receive için geçersiz uzunluk")
            break
    elif ifade[0] == "send":
        if len(ifade) - 1 == 4:
            sinyal = int(ifade[1])
            cihaz = int(ifade[2])
            durum = int(ifade[3])
            cevap = int(ifade[4])
            if sinyal < 0 or sinyal > 255:
                print("Error : birinci bölüm hatalı")
            if cihaz < 0 or cihaz > 4:
                print("Error : ikinci bölüm hatalı")
            if durum < 0 or durum > 1:
                print("Error : üçüncü bölüm hatalı")
            if cevap < 0 or cevap > 1:
                print("Error : dördüncü bölüm hatalı")
            else:
                print("Kod Tipi : send - Giden")
                if (sinyal >= 0 and sinyal <= 50):
                    print("Sinyal Gucu : ", ifade[1], " - Çok Zayıf ")
                elif (sinyal >= 51 and sinyal <= 100):
                    print("Sinyal Gucu : ", ifade[1], " - Zayıf Sinyal")
                elif (sinyal >= 101 and sinyal <= 150):
                    print("Sinyal Gucu : ", ifade[1], " - Orta Sinyal")
                elif (sinyal >= 151 and sinyal <= 200):
                    print("Sinyal Gucu : ", ifade[1], " - Güçlü Sinyal")
                elif (sinyal >= 201 and sinyal <= 255):
                    print("Sinyal Gucu : ", ifade[1], " - Çok Güçlü Sinyal")
                if (cihaz == 1):
                    print("Cihaz : 1 - Televizyon")
                elif (cihaz == 2):
                    print("Cihaz : 2 - Camasir Makinesi")
                elif (cihaz == 3):
                    print("Cihaz : 3 - Buzdolabi")
                elif (cihaz == 4):
                    print("Cihaz : 4 - Firin")
                if (durum == 0):
                    print("Durum : 0 - Off")
                elif (durum == 1):
                    print("Durum : 1 - On")
                if (cevap == 0):
                    print("Cevap : 0 - İstenmiyor")
                elif (cevap == 1):
                    print("Cevap : 1 - İsteniyor")
        else:
            print("Error : send için geçersiz uzunluk")
            break
    else:
        print("Error: geçersiz ifade")
        break
    if i + 1 != len(ifadeler) - 1:
        print("------")
