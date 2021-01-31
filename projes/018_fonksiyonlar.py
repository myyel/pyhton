
# fonksiyon kullanımı

def bes_bastir():
    print(5)
    
bes_bastir()

# parametre döndüren fonksiyonlar

def bes_dondur():
    return 5

x=bes_dondur()
print(x)


def buyuk_sayi_dondur(a=1,b=0):    #default değerler atandı. eğer fonsiyona çağrılırken
    if a>b:                         #herhangi bir parametre gönderilmezse a=1 ve b=0 olacak.
        return a
    elif b>a:
        return b
    else:
        return "sayılar birbirine eşit"
    
x=buyuk_sayi_dondur(3,6)
print(x)
y=buyuk_sayi_dondur()
print(y)

# args kullanımı

def isim_birlestir(*args):
    return "-".join(args)        # "-" ile gelen parametleri birleştiriyor

x=isim_birlestir("mehmet", "yasin","yel")
print(x)

#kwargs kullanımı

def gobek_adi_yazdir(**kwargs):
    if "gobek_adi" in kwargs:
        print(kwargs["gobek_adi"])
    else:
        print("Göbek adı yok")
        
gobek_adi_yazdir(adi="mehmet",gobek_adi="yasin",soyadi="yel")


