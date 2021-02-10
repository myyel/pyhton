
# requests module - post methodu

import requests

#https://image-charts.com/chart?cht=bb&chd=t:10,10,30,_,30,40,35&chf=b0,lg,90,03a9f47C,0,3f51b57C,1&chxt=y,x&chs=711x313&chl=label%201|label%202&chma=0,50,50&chg=20,20" alt="Static Chart

adres="https://image-charts.com/chart"

argms={
       "chs":"700x190",
       "chd":"t:60,40",
       "cht":"p3",
       "ch1":"Hello|World",
       "chan":None,
       "chf":"ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1"
       }

cevap=requests.post(adres, data=argms)

print(cevap.status_code)
print(cevap.content)

from PIL import Image
from io import BytesIO

resim=Image.open(BytesIO(cevap.content))
print(resim.show())
