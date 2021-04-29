k1=input("1.kenar: ")
while not k1.isdigit():
    print("lütfen sayı giriniz")
    k1=input("1.kenar: ")
k2=input("2.kenar: ")
while not k2.isdigit():
    print("lütfen sayı giriniz")
    k2=input("2.kenar: ")
k3=input("3.kenar: ")
while not k3.isdigit():
    print("lütfen sayı giriniz")
    k1=input("3.kenar: ")
    
while abs(int(k1)-int(k2))>int(k3) or abs(int(k2)-int(k3))>int(k1) or abs(int(k1)-int(k3))>int(k2):
    print("girilen değerlerle üçgen oluşturulamaz")
    k1=input("1.kenar: ")
    while not k1.isdigit():
        print("lütfen sayı giriniz")
        k1=input("1.kenar: ")
    k2=input("2.kenar: ")
    while not k2.isdigit():
        print("lütfen sayı giriniz")
        k2=input("2.kenar: ")
    k3=input("3.kenar: ")
    while not k3.isdigit():
        print("lütfen sayı giriniz")
        k1=input("3.kenar: ")
        
if k1==k2==k3:
    print("eş kenar üçgen")
elif k1==k2 or k2==k3 or k3==k1:
    print("ikizkenar üçgen")
else:
    print("çeşitkenar üçgen")

    