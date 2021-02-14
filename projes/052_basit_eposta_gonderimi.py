import ssl
import smtplib

kullanici_adi="hesap@gmail.com"
sifre="asdjaskda"

alici="hesap@hotmail.com"

mesaj="deneme"

icerik=ssl.create_default_context()

port_no=465        

host_isim="smtp.gmail.com"

eposta_sunucusu=smtplib.SMTP_SSL(host=host_isim, port=port_no, context=icerik)

eposta_sunucusu.login(kullanici_adi,sifre)

eposta_sunucusu.sendmail(kullanici_adi,alici,mesaj)




