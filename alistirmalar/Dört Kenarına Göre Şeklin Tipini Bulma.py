k1=input("1. kenar: ")
while not k1.isdigit():
    print("lütfen bir sayi giriniz")
    k1=input("1. kenar: ")

k2=input("2. kenar: ")
while not k2.isdigit():
    print("lütfen bir sayi giriniz")
    k2=input("2. kenar: ")
    
k3=input("3. kenar: ")
while not k3.isdigit():
    print("lütfen bir sayi giriniz")
    k3=input("3. kenar: ")
    
k4=input("4. kenar: ")
while not k4.isdigit():
    print("lütfen bir sayi giriniz")
    k4=input("4. kenar: ")
    
if k1==k2==k3==k4:
    print("kare")
elif k1==k2 and k3==k4 or k1==k3 and k2==k4 or k1==k4 and k2==k3 :
    print("dikdörgen")
else:
    print("dörtgen")5