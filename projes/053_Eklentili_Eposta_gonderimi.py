import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

kullanici_adi="hesap@gmail.com"
sifre="asdjaskda"

alici="hesap@hotmail.com"

mesaj="deneme"

baslik="Python_learn"

icerik=ssl.create_default_context()

posta=MIMEMultipart()
posta["From"]=kullanici_adi
posta["To"]=alici
posta["Subject"]=baslik

posta.attach(MIMEText(mesaj, "plain"))

eklenti_dosya_isimi="resim.jpg"

with (open(eklenti_dosya_isimi,"rb")) as eklenti_dosyasi:
    payload=MIMEBase("application", "octate-stream")
    payload.set_payload(eklenti_dosyasi.read())
    encoders.encode_base64(payload)
    
    payload.add_header("Content-Decomposition", "attachment", filename=eklenti_dosya_isimi)
    posta.attach(payload)
    
    posta_str=posta.as_string()
    
port_no=465        

host_isim="smtp.gmail.com"

eposta_sunucusu=smtplib.SMTP_SSL(host=host_isim, port=port_no, context=icerik)

eposta_sunucusu.login(kullanici_adi,sifre)

eposta_sunucusu.sendmail(kullanici_adi,alici,posta_str)



