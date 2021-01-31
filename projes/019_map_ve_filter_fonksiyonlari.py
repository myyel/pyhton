# map kullanımı

def kare_al(sayi):
    return sayi*sayi

sayilar=[*range(1,6)]

sonuc=[*map(kare_al,sayilar)]
print(sonuc)

# filter kullanımı

def cift_sayilari_goster(x):
    if x%2==0:
        return x
    
sayilar=[*range(1,21)]
print([*filter(cift_sayilari_goster,sayilar)])

