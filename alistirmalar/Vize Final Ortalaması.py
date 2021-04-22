def harf_notunu_bul(vize1,vize2,final):
    if vize1.isdigit() and vize2.isdigit() and final.isdigit():        
        toplam=(int(vize1)*0.3)+(int(vize2)*0.3)+(int(final)*0.5)
        print(toplam)
        if toplam >= 0 and toplam < 10:
            print("Notunuz: FF")
        elif toplam>10 and toplam<20:
            print("Notunuz: FD")
        elif toplam>20 and toplam<30:
            print("Notunuz: DF")
        elif toplam>30 and toplam<40:
            print("Notunuz: DD")
        elif toplam>40 and toplam<50:
            print("Notunuz: DC")
        elif toplam>50 and toplam<60:
            print("Notunuz: CC")
        elif toplam>60 and toplam<70:
            print("Notunuz: CB")
        elif toplam>70 and toplam<80:
            print("Notunuz: BB")
        elif toplam>80 and toplam<90:
            print("Notunuz: BA")
        elif toplam>90 and toplam<100:
            print("Notunuz: AA")    
        else:
            print("girilen değerler yanlıştır")
    else:
        print("girilen değerler yanlıştır")
        

vize1=input("1.vize notunuzu giriniz: ")
vize2=input("2.vize notunuzu giriniz: ")
final=input("final notunuzu giriniz: ")

harf_notunu_bul(vize1,vize2,final)
