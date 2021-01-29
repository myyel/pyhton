# break kullanımı

harfler=["a","b","c","d","e"]*100

for inx, harf in enumerate(harfler):
    if harf=="b":
        print(inx+1, ". harf: ",harf)
        break                #b harfini bulup yazdırdıktan sonra döngüyü kıracak
        
# continue kullanımı

for sayi in range(1,6):
    if sayi%2==0:
        continue  # buraya geldiğinde 2'ye bölünebilen sayıları geçip döngüye devam edecek
    print(sayi)
    
# pass kullanımı

for sayi in range(1,6):
    if sayi%2==0:
        pass
    else:
        print(sayi)