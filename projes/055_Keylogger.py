from pynput.keyboard import Listener,Key

def bas(key):
    try:
        print(key.char, type(key.char))
    except:
        pass

def birak(key):

    print("tuş bırakıldı")


with Listener(on_press=bas, on_release=birak) as dinleyici:


    dinleyici.join()


    12