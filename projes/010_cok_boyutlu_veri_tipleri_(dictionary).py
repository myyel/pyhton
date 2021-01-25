 dict1={
       "isim":"mehmet",
       "soyisim":"yel",
       "yaş":33,
       "lokasyon":"eskişehir"
       }
print(dict1)
print(dict1["yaş"])

dict2 = {
        "isim":"mehmet",
        "soyisim":"yel",
        "yaş":33,
        "lokasyon":{
            "doğduğu şehir":"söğüt",
            "yaşadığı şehir":"eskişehir"
            }
    }

print(dict2["lokasyon"]["yaşadığı şehir"])

print(dict2.keys()) #anahtarları döndürüyor

print(dict2.values()) #değerleri döndürüyor
      
print(dict2.items()) #hem anahtarları hem de değerleri birlikte döndürüyor
