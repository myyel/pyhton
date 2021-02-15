
from imap_tools import MailBox

posta_kutusu=MailBox("imap.gmail.com")

posta_kutusu.login(kullanici,sifre,initial_folder="INBOX")

import datetime
from imap_tools import AND

kriter=AND(date_gte=datetime.date(2021,1,1), from_=kullanici)

for msg in posta_kutusu.fetch(kriter):
    print(msg.text)

