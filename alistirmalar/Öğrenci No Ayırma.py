ogrenci_no=input("öğrenci numarası: ")
while not ogrenci_no.isdigit(): 
    print("yanlış bir değer girdiniz")
    ogrenci_no=input("öğrenci numarası: ")
    while len(ogrenci_no)!=12:
        print("yanlış bir değer girdiniz")
        ogrenci_no=input("öğrenci numarası: ")

liste=list(ogrenci_no)
i=0
z=""
while i<4:
    for x in liste:
        z=z+x
        i+=1
        if i==4:
            giris_yili=z
            z=""
        elif i==6:
            fakulte_no=z
            z=""
        elif i==8:
            bolum_no=z
            z=""
        elif i==10:
            ogrenim_no=z
            z=""    
        elif i==12:
            giris_no=z
            z=""
print("giriş yılı: {0}\nfakülte numarası: {1}\nbölüm numarası: {2}\nöğrenim numarası: {3}\ngiriş numarası: {4}\n".format(giris_yili, fakulte_no,bolum_no, ogrenim_no,giris_no))