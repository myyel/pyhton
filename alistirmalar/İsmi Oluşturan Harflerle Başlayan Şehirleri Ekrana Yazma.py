import re

iller=[
       "adana","adıyaman", "afyonkarahisar", "ağrı","aksaray", "amasya","ankara", "antalya","ardahan","artvin",
      "aydın", "balıkesir","bartın","batman","bayburt","bilecik","bingöl","bitlis","bolu","burdur","bursa",
      "çanakkale","çankırı","çorum","denizli","diyarbakır","düzce", "edirne","elazığ","erzincan","erzurum",
      "eskişehir","gaziantep","giresun","gümüşhane","hakkari","hatay","ığdır","ısparta","istanbul","izmir",
      "kahramanmaraş","karabük","karaman","kars","kastamonu","kayseri","kilis","kırıkkale","kırklareli",
      "kırşehir","kocaeli","konya","kütühya","malatya","manisa","mardin","mersin","muğla","muş","nevşehir",
      "niğde","ordu","osmaniye","rize","sakarya","samsun","şanlıurfa","siirt","sinop","şırnak","sivas","tekirdağ",
      "tokat","trabzon","tunceli","uşak","van""yalova","yozgat","zonguldak"
      ]

liste=[]
isim=list(input("isminiz: "))

for harf in isim:
    patern=r"^{0}".format(harf)
    for il in iller:
        for eslesme in re.finditer(patern, il):
            if len(eslesme.group())>0:
               liste.append(il) 
               
for a in liste:
    print(a)
