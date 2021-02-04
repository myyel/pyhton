
# os module ekleniyor
import os

print(os.getcwd())  #mevcut dosyanın bulunduğu adresi veriyor

print(os.listdir())   # mevcut dosyanın bulundğu klasördeki dosyalri listeliyor

print(os.listdir("d:/masaüstü/python"))  # belirtilen adresteki klasörün içindeki dosyaları listeliyor

print(os.chdir("d:/masaüstü/python"))   # dosyanın adresini belirtilen adres olarak gösteriyor.

os.mkdir(os.getcwd()+"/merhaba")          # klasör oluşturma make directory
os.mkdir("d:/masaüstü/python/merhaba2")   # yukarıdakinin aynısı

os.rmdir(os.getcwd()+"/merhaba")          # klasör silme(içi boş ise silinir, 
# yoksa içindekiler silinip sonra klasör siliniyor. ama başka bir modülde hepsi bir anda silinebiliyor)



## os.O_RDONLY − Read Only      - Sadece Okuyor
## os.O_WRONLY − Write Only     - Sadece Yazıyor
## os.O_RDWR   − Read and Write - Okuyor ve Yazıyor
## os.O_CREAT  - Create         - Olusturuyor

yeni_dosya = os.open('yeni_dosya.txt', os.O_RDWR|os.O_CREAT)
os.write(yeni_dosya, "Merhaba dünya!".encode())
os.close(yeni_dosya)

yeni_dosya = os.open('yeni_dosya.txt', os.O_RDONLY)
uzunluk = os.stat(yeni_dosya).st_size
icerik = os.read(yeni_dosya,uzunluk)
print(icerik.decode())
os.close(yeni_dosya)


os.unlink("yeni_dosya.txt")                      # dosya silme

os.mkdir("deneme_yeni")

os.renames("deneme_yeni", "deneme_eski")         # dosya ismini değiştirme
