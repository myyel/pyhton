def cevre(r,pi=3.14):
    cev=2*pi*int(r)
    print(cev)
def alan(r,pi=3.14):
    al=pi*int(r)*int(r)
    print(al)
    
r=input("yarıçap: ")
while not r.isdigit():
    print("bir sayı değeri giriniz")
    r=input("yarıçap: ")


islem=input("1-Alan   2-Çevre\n")
while not islem.isdigit():
    print("belirtilen değerlerden birini giriniz")
    islem=input("1-Alan   2-Çevre\n")
    
while not islem=="1":
    if islem=="2":
        break
    else:
        print("belirtilen değerlerden birini giriniz")
        islem=input("1-Alan   2-Çevre\n")
    
if islem=="1":
    alan(r)
elif islem=="2":
    cevre(r)
else:
    print("bir hata oluştu, lütfen tekrar giriniz")