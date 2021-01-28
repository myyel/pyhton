
#for döngüsü kullanımı
ogrenci_listesi=[
    "altay demir",
    "ebru karaca",
    "efe kanbil", 
    "efe tosun",
    "nursima çukur",
    "güner özten", 
    "serhat doğan", 
    "mehmet yel",
    "ela durmuş"]
ogrenci_no=0

for x in ogrenci_listesi:
    ogrenci_no+=1   
    print(ogrenci_no,x)
    
    
    
#iç içe listelerde for döngüsü

liste=[[1,2,7],[3,4,8],[5,6,9]]  #iç listede 3 değer oludğu için döngüde 3 değişken olmalı

for x,y,z in liste:
    print((x+y)*z)
    
    

#dictinary dizisinde for döngüsü

dict1={
       "ad":"mehmet",
       "soyad":"yel"
       }

for k,v in dict1.items():
    print(k+"= ",v)
    