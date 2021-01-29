
#range kullanımı
x=[*range(10)]
print(x)

x=[*range(3,6)]  #3 ile 6 arasındaki sayıları döndürecek. 3'ü kapsayacak ama 6'yı kapsamayacak
print(x)

#enumerate kullanımı
harfler=["a","b","c","d","e"]

for harf in enumerate(harfler):
    print(harf)

    
for index, harf in enumerate(harfler): #ayrı ayrı bastırılabilir
    print(index)
    print(harf)
    print(index,harf)
    
#zip

ulkeler=["tr","fr","de"]
siralama=range(1,4)

for ulke in zip(siralama,ulkeler):
    print(ulke)
        
