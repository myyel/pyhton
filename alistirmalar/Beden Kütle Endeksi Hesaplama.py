def bde(kilo, boy):
    ke=10000*kilo/(boy*boy)
    print(ke)
    if ke<18.5: 
        print("zayıf")
    elif 25>=ke>18.5: 
        print("Normal")
    elif 30>=ke>25: 
        print("Kilolu")
    elif ke>30:     
        print("Obez")
        

try:
    kilo=int(input("Kilonuzu giriniz: "))
    boy=int(input("Boyunuzu cm cinsinden giriniz: "))
    while boy<50:
        print("yanlış bir değer girdiniz")
        boy=int(input("Boyunuzu cm cinsinden giriniz: "))
    
    bde(kilo, boy)
except:
    print("yanlış bir değer girdiniz")
    