def cevre_bul(uk,kk):
    cevre=2*(int(uk)+int(kk))
    return cevre

def alan_bul(uk,kk):
    alan= int(uk)*int(kk)
    return alan


uk=input("uzun kenar: ")
while not uk.isdigit():
    print("bir sayı değeri giriniz")
    uk=input("uzun kenar: ")
    
kk=input("kısa kenar: ")
while not kk.isdigit():
    print("bir sayı değeri giriniz")
    kk=input("kısa kenar: ")
    
while kk>uk:
    print("uzun kenar, kısa kenardan büyük olmalıdır...")
    uk=input("uzun kenar: ")
    while not uk.isdigit():
        print("bir sayı değeri giriniz")
        uk=input("uzun kenar: ")
    
    kk=input("kısa kenar: ")
    while not kk.isdigit():
        print("bir sayı değeri giriniz")
        kk=input("kısa kenar: ")
    
cevre= cevre_bul(uk, kk)
alan= alan_bul(uk, kk)

print("alan: {0}\nçevre: {1}".format(alan,cevre))