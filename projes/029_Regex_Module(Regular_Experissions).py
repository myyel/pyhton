 # regex kullanımı

import re

cumle="Mustafa Kemal Atatütk, Türk asker, devlet adamı ve Türkiye Cumhuriyeti'nin kurucusudur."

patern="Türk"

print(re.search(patern, cumle))

durum=re.search(patern, cumle)
print(durum.span())
print(durum.start())
print(durum.end())


for eslesme in re.finditer(patern, cumle):
    print(eslesme.span(),eslesme.group())
    

print(re.search("Kemal\s\w\D\w", cumle))