
# inheritance in classes

class Seyehat():
    def __init__(self, kalkis,  varis):
        self.kalkis=kalkis
        self.varis=varis
        
    def anons(self):
        return "{}-{} seyehatine hoşgeldibiz".format(self.kalkis,self.varis)
    
class Otobus(Seyehat):
    def __init__(self, mola_duraklari, kalkis, varis):
        Seyehat.__init__(self, kalkis, varis)
        self.mola_duraklari=mola_duraklari
        
        
seyehat1=Seyehat("bil", "ist")
print(seyehat1.anons())

oto1=Otobus(["pamuk"], "ist","ank")
print(oto1.mola_duraklari)