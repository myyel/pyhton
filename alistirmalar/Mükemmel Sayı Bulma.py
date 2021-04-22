def mukemmel_bul(sayi):
    i=1
    toplam=0
    while not i==sayi:
        if sayi%i==0:
            toplam+=i
        i+=1
    
    if toplam==sayi:
        print(sayi," sayısı mükemmel sayıdır")
    else:
        print(sayi," sayısı mükemmel sayı değildir")
        
sayi=int(input("bir sayı giriniz: "))
mukemmel_bul(sayi)
        
        
        