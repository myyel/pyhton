a=12
b=3
toplam=a+b

#durum 1
if toplam==15:
    print("sonuç doğru, sonuç:",toplam) #durum 1
    
hava="karlı"

#durum 2
if hava=="yağışlı":
    print("şemsiye al")

else:
    print("dışarı çıkma")

# durum 3

not1=75
not2=60
ort=(not1+not2)/2

if  ort>=70:
    print("geçti")
    
elif ort>=40 and ort<70:
    print("şartlı geçti")
    
else:
    print("kaldı")
    
    
# list veri tipinin içinde if sorgusuyla ve in operatörü ile eleman arama

liste=["a","b","c"]
hedef_harf="d"

if hedef_harf in liste:
    print("harf mevcut")
else:
    liste.append(hedef_harf)  #harf liste dizisine eklenecek
    print("harf eklendi")
    print("yeni liste: ",liste)
    
    

