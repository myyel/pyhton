def poz_bol_bul(sayi):
    liste=[]
    
    for i in range(1, sayi+1):
        if sayi%i==0:
            liste.append(i)
    return print(liste)
            
         
sayi=int(input("Bir sayı giriniz: "))
poz_bol_bul(sayi)