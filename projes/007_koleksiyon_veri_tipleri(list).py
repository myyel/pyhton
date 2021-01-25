liste=[1,2,"s",4,"s",0.5]

liste=liste+[1]

print(liste)

liste.append(3) #yukarıdakinin aynısı, append eleman eklemek
print(liste)

liste.pop() #son list'deki son veriyi kaldırıyor
print(liste)

liste.pop(4) #4.indisdeki veriyi kaldıracak
print(liste)

sayilar=[23,54,12,76,34,98,46]
sayilar.reverse()
print(sayilar) # dizi sırasını tersine çeviriyor

sayilar.sort()
print(sayilar) #sayıları sıralıyor ve indis numaraları da değişiyor