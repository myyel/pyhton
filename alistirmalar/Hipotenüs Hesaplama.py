from math import sqrt
try:
    a=int(input("birinci kenarı giriniz: "))     
    b=int(input("ikinci kenarı giriniz: "))     
except:
    print("yanlış bir değer girdiniz")
    
print(sqrt(a**2+b**2))