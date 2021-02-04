# class yapısı

# class'a özgü attribute'lar

class Ucus():
    havayolu="THY"
    

fly=Ucus()
print(fly.havayolu)


#  Objeye özgü atrribute'lar

class Ucus2():
    havayolu2="Pegasus"
    
    def __init__(self,kod,kalkis,varis,saat,kapasite,yolcu_sayisi):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.saat=saat
        self.kapasite=kapasite
        self.yolcu_sayisi=yolcu_sayisi
        
        
fly2=Ucus2(123,"ist","ank","22:50",300,160)

print(fly2.varis)
print(fly2.havayolu2)

# class'ta methodlar

class Ucus3():
    havayolu2="Pegasus"
    
    def __init__(self,kod,kalkis,varis,saat,kapasite,yolcu_sayisi):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.saat=saat
        self.kapasite=kapasite
        self.yolcu_sayisi=yolcu_sayisi
        
    def anans_yap(self):
        anons=(self.kod," sefer sayılı ",self.kalkis,"-",self.varis," uçuşumuz saat ",self.saat,"de gerçekleşecektir")
        return anons
    
fly3=Ucus3(123,"ist","ank","22:50",300,160)
print(fly3.anans_yap())
        