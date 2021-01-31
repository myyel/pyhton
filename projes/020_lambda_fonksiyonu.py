# lambda kullanımı

def kare_al(x):
    return x*x

sayilar=[*range(1,21)]
print([*map(kare_al,sayilar)])

#yukarıdaki fonksiyonun kısa yolu için lambda kullanılıyor.

sayilar2=[*range(1,21)]
a=[*map(lambda x : x*x,sayilar2)]
print(a)