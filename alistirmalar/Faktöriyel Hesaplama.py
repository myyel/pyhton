def faktoriyel(sayi):
    toplam=1
    for i in range(int(sayi)):
        i+=1
        toplam=i*toplam
        
    print(toplam)
    
    
sayi=input("sayı:")
while not sayi.isdigit():
    print("bu sayı değil")
    sayi=input("sayı:")
    
faktoriyel(sayi)