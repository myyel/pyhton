
# decorator'lar

#bir fonksiyon değişkene atanabilir
def fon():      
    print("merhaba")
    
f=fon

f()

#bir fonksiyonun içinde başka bir fonksiyon olabilir
def tanisma(a):
    print("merhaba")
    
    def isim(x):
        return "benim adım "+x
    
    print(isim(a))        
        
tanisma("mehmet")

#bir fonksiyon arguman olarak başka bir fonksiyona gönderilebilir

def deneme1():
    return "deneme1 çalışıyor"
    
def deneme2(f):
    print("deneme2 çalışıyor")
    print(f())
    
deneme2(deneme1)

# deco örnek

def deco(f):
    def wrapper():
        print("başlangıç")
        f()
        print("bitiş")
        
    return wrapper 

def yazdir():
    print("merhaba")
    
x=deco(yazdir)
x()

@deco 
def yazdir2():
    print("slm")
    
yazdir2()

#deco arguman alan fonksiyonlarda 

def deco2(f):
    def wrapper(*args):
        print("başlangıç")
        f(*args)
        print("bitiş")
        
    return wrapper 

@deco2 
def toplama(a,b):
    print(a+b)
    
toplama(4, 5)

# deco arguman alan decorator'larda
import time

def deco3(msg1,msg2):
    def ara_katman(f):
        def wrapper(*args):
            print(msg1)
            f(*args)
            print(msg2)
            
        return wrapper
    return ara_katman

@deco3("Merhaba","Sayısı")
def toplama(a,b):
    print(a+b)
    
toplama(7,9)

# deco örnek

def sure_olc(f):
    def wrapper(*args):
        baslangic=time.time()
        f(*args)
        bitis=time.time()
        print(bitis-baslangic)
    return wrapper 

@sure_olc 
def faktoriyel(a):
    toplam=1
    while(a>1):
        toplam=a*toplam
        a-=1
    
faktoriyel(200000)
    
