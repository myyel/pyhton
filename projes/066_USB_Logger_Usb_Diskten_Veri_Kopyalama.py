import os

for klasor_yolu,klasor_ismi,dosya_ismi in os.walk("C:/Users/Casper/Desktop"):
    print("klasor_yolu: ",klasor_yolu)
    print("klasor_ismi: ",klasor_ismi)
    print("dosya_ismi",dosya_ismi)



