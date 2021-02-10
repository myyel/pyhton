
# Request Module

import requests

print(requests.get("https://data.police.uk/docs/method/forces/"))

print(requests.get("https://data.police.uk/docs/method/forces/").status_code)

print(requests.get("https://data.police.uk/docs/method/forces/").url)

#print(requests.get("https://data.police.uk/docs/method/forces/").text)


adres="https://data.police.uk/api/crime-categories"
parametre={"date":"2019-05"}

print(requests.get(adres, parametre))

#print(requests.get(adres, parametre).text)
print(requests.get(adres, parametre).url)

print(requests.get(adres, parametre).json())


uzanti="https://data.police.uk/api/crimes-no-location"

argums ={
         "category": "all-crime",
         "force":"city-of-london",
         "date":"2020-01"}
    
print(requests.get(uzanti, params=argums).text)