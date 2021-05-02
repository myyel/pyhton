def toplama(s1,s2):
    t=int(s1)+int(s2)
    print(t)
    
def cikarma(s1,s2):
    t=int(s1)-int(s2)
    print(t)
    
def carpma(s1,s2):
    t=int(s1)*int(s2)
    print(t)
    
def bolme(s1,s2):
    t=int(s1)/int(s2)
    print(t)
    
s1=input("1. sayı: ")
while not s1.isdigit():
    print("bir sayı değeri giriniz")
    s1=input("1. sayı: ")

s2=input("2. sayı: ")
while not s2.isdigit():
    print("bir sayı değeri giriniz")
    s2=input("2. sayı: ")
    
deger=input("yapılacak olan işlemi girin\n1-toplama   2-çıkarma   3-çarpma   4-bölme\n")
while not deger.isdigit():
    print("lütfen belirtilen değerler arasında bir değer giriniz")
    deger=input("yapılacak olan işlemi girin\n1-toplama   2-çıkarma   3-çarpma   4-bölme\n")
    
if deger=="1":
    toplama(s1, s2)
elif deger=="2":
    cikarma(s1, s2)
elif deger=="3":
    carpma(s1, s2)
elif deger=="4":
    bolme(s1, s2)
else:
    print("bir hata oluştu, lütfen tekrar deneyiniz")