def permutasyon(n,r):
    nt=1
    rt=1
    for i in range(int(n)):
        i+=1
        nt=nt*i
    r=int(n)-int(r)
    for i in range(int(r)):
        i+=1
        rt=rt*i
    
    print(nt/rt)
    
    
n=input("asıl küme sayısı: ")
while not n.isdigit():
    print("bir sayı değeri giriniz")
    n=input("asıl küme sayısı: ")
r=input("alt küme sayısı: ")
while not r.isdigit():
    print("bir sayı değeri giriniz")
    r=input("alt küme sayısı: ")
permutasyon(n, r)