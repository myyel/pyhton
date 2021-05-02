def kombinasyon(n,r):
    nt=1
    rt=1
    zt=1
    for i in range(int(n)):
        i+=1
        nt=nt*i
    for i in range(int(r)):
        i+=1
        rt=rt*i
    
    
    z=int(n)-int(r)
    for i in range(z):
        i+=1
        zt=zt*i
    
    print(nt/(rt*zt))
    
n=input("asıl küme sayısı: ")
while not n.isdigit():
    print("bir sayı değeri giriniz")
    n=input("asıl küme sayısı: ")
r=input("alt küme sayısı: ")
while not r.isdigit():
    print("bir sayı değeri giriniz")
    r=input("alt küme sayısı: ")
    
kombinasyon(n, r)