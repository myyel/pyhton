
# try-except yapısı

def tam_sayiya_cevir():
    girdi=input("bir ondalık sayı gir: ")
    statu=""
    try:
        girdi=round(float(girdi))
        print(girdi,"'na dönüştürüldü")
        statu="başarılı"
    except:
        print(girdi,"dönüştürülemedi")
        statu="başarısız"
    finally:
        print(statu)
        
tam_sayiya_cevir()

        
 # except hata tipi

try:
    s="b"
    x=5+s
    print(x)
except TypeError:                     # TypeError hatası olduğunda aşağıdaki kod çalışacak
    print("işlem başarısız")