from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox

pencere=Tk()

def gonder():
    son_mesaj=""

    try:
        if var.get():
            if var.get()==1:
                son_mesaj="Veriniz başarıyla sisteme kaydedilmiştir"
                messagebox.showinfo("Başaarılı İşlem", son_mesaj)

                tip= hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get()=="" else "Genel"
                tarih2=tarih.get()
                mesaj2=metin.get("1.0","end")    

                with open("hatir.txt","w") as dosya:
                    dosya.write(
                        tip+" kategorisinde,"+tarih2+" tarihine ve "+mesaj2+" notuyla hatırlatma")
                    dosya.close()
            elif var.get()==2:
                son_mesaj="E-Posta yoluyla hatırlatma size ulaşacaktır."
                messagebox.showinfo("Başaarılı İşlem", son_mesaj)
        else:
            son_mesaj="Gerekli alanların doldurulduğuna emin olun"
            messagebox.showwarning("Başaarısız İşlem", son_mesaj)
    except:
        son_mesaj="Hata oluştu"
        messagebox.showerror("Başaarısız İşlem", son_mesaj)
    finally:
        pencere.destroy()

cnvs=Canvas(pencere, height=450, width=750)
cnvs.pack()

panel_ust=Frame(pencere, bg='#add8e6')
panel_ust.place(relx=0.05, rely=0.05, relwidth= 0.9, relheight=0.10)

panel_alt_sol = Frame(pencere, bg='#add8e6')
panel_alt_sol.place(relx=0.05, rely=0.18, relwidth= 0.33, relheight=0.75)

panel_alt_sag = Frame(pencere, bg='#add8e6')
panel_alt_sag.place(relx=0.40, rely=0.18, relwidth= 0.55, relheight=0.75)

etiket_hatirlatma=Label(panel_ust, bg="#add8e6", text="Hatırlatma Tipi:", font="Verdana 12 bold") 
etiket_hatirlatma.pack(padx=10, pady=10, side=LEFT) 

hatirlatma_tipi_opsiyon=StringVar(panel_ust)
hatirlatma_tipi_opsiyon.set("\t")

hatirlatma_tipi_list=OptionMenu(panel_ust, hatirlatma_tipi_opsiyon,"Doğum Günü","Alışveriş","Ödeme")
hatirlatma_tipi_list.pack(padx=10, pady=10, side=LEFT)

tarih=DateEntry(panel_ust, width=12, background="orange", foreground="black",borderwidth=1, locale="de")
tarih._top_cal.overrideredirect(False)
tarih.pack(padx=10, pady=10, side=RIGHT)

etiket_hatirlatma=Label(panel_ust, bg="#add8e6", text="Hatırlatma Tarihi:", font="Verdana 12 bold") 
etiket_hatirlatma.pack(padx=10, pady=10, side=RIGHT)

Label(panel_alt_sol, bg="#add8e6", text="Hatırlatma Yöntemi:", font="Verdana 12 bold").pack(padx=10, pady=10, anchor=N)

var=IntVar()

r1=Radiobutton(panel_alt_sol, text="Sisteme Kaydet", variable=var, value=1, bg="#add8e6", font="Verdana 10")
r1.pack(anchor=N, pady=5,padx=15)

r2=Radiobutton(panel_alt_sol, text="E-Posta gönder", variable=var, value=2, bg="#add8e6", font="Verdana 10")
r2.pack(anchor=N, pady=5,padx=15)

var1=IntVar()
c1=Checkbutton(panel_alt_sol, text="Bir gün önce",variable=var1, onvalue=1, offvalue=0,bg="#add8e6", font="Verdana 11")
c1.pack(anchor=NW, pady=5,padx=25)

var2=IntVar()
c2=Checkbutton(panel_alt_sol, text="Bir hafta önce",variable=var2, onvalue=1, offvalue=0,bg="#add8e6", font="Verdana 11")
c2.pack(anchor=NW, pady=5,padx=25)

var3=IntVar()
c3=Checkbutton(panel_alt_sol, text="Aynı gün",variable=var3, onvalue=1, offvalue=0,bg="#add8e6", font="Verdana 11")
c3.pack(anchor=NW, pady=5,padx=25)

Label(panel_alt_sag, bg="#add8e6", text="Hatırlatma Mesajı:", font="Verdana 12 bold").pack(padx=10, pady=10, anchor=N)

metin=Text(panel_alt_sag, height=13, width=45, background="#dee2b6")
metin.tag_configure("style",foreground="#bfbfbf", font=("Verdana",9,"bold"))
metin.pack()

karsilama="Mesajınızı giriniz..."
metin.insert(END, karsilama,"style")

buton=Button(panel_alt_sag, text="Gönder", command=gonder)
buton.pack(anchor=S)

pencere.mainloop();