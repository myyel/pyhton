
# input() kullanımı

a=input("bir sayı gir: ")
print(type(int(a)))

# input() komutuyla bir uygulama

def dogrula():
    sayi=input("bir sayi giriniz")
    cevap=input(" tek mi, çift mi?")
    if int(sayi)%2==0:
        if cevap=="tek":
            print(" sayısı bir çift sayıdır")
        
        elif cevap=="çift":
            print(" doğru cevap")
        
        else:
            print("hata")
            
    elif int(sayi)%2!=0:
        if cevap=="tek":
            print("doğru cevap")
        
        elif cevap=="çift":
            print(" sayısı bir çift sayıdır")
        
        else:
            print("hata")
            
    else:
        print("hata")


dogrula()
