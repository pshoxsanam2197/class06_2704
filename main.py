# 23-m
class Kiyim:
    def __init__(self, nomi):
        self.nomi = nomi

    def kiyish(self):
        print("Kiyildi")

class Kurtka(Kiyim):
    def kiyish(self):
        print("Kurtka kiyildi")

ota = Kiyim("Kiyim")
ota.kiyish()

bola = Kurtka("Kurtka")
bola.kiyish()

24-m
class Talaba:
    def __init__(self,ism):
        self.ism = ism

    def oqish(self):
        print("O'qimoqda")

class ITtalaba(Talaba):
    def oqish(self):
        print("Dasturlash o'qimoqda")

ota = Talaba("Talaba")
ota.oqish()

bola = ITtalaba("ITtalaba")
bola.oqish()
