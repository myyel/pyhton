def asal_bul(s1,s2):
    liste=[]
    if int(s1)>int(s2):
        while not int(s2)>int(s1):
           for i in range(int(s2)):
               i+=1
               if i==1:
                   i+=1
                   pass
               else:
                   if int(s2)%i==0:
                       if i==int(s2):
                           liste.append(s2)
                       else:
                           break
                   else:
                       i+=1
            
           s2=int(s2)+1
    elif int(s2)>int(s1):
        while not int(s1)>int(s2):
           for i in range(int(s1)):
               i+=1
               if i==1:
                   i+=1
                   pass
               else:
                   if int(s1)%i==0:
                       if i==int(s1):
                           liste.append(s1)
                       else:
                           break
                   else:
                       i+=1
            
           s1=int(s1)+1

    print(liste)
    

s1=input("1.sayı: ")
while not s1.isdigit():
    print("lütfen bir sayı giriniz")
    s1=input("1.sayı: ")

s2=input("2.sayı: ")
while not s2.isdigit():
    print("lütfen bir sayı giriniz")
    s1=input("2.sayı: ")

asal_bul(s1,s2)
    
