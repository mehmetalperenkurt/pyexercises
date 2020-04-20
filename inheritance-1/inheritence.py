class Cokgen():
    def __init__(self,kenar_sayisi):
        print("Yapıcı metodu çalıştırıldı.")
        self.n=kenar_sayisi
        self.kenarlar=[]

    def uzunlukGir(self):
        self.kenarlar=[float(input(str(i+1)+". Kenar : ")) for i in range(self.n)]
    def cevreHesapla(self):
        print("Cevre :",sum(self.kenarlar))
b=int(input("kenar sayısını girin "))
while(b<3):
    b = int(input("kenar sayısını girin "))
a=Cokgen(b)
class Ucgen(Cokgen):
    def __init__(self):
        Cokgen.__init__(self,3)
    def alanHesapla(self):
        a,b,c=self.kenarlar
        u=(a+b+c)/2
        alan=(u*(u-a)*(u-b)*(u-c))*0.5
        print("Ucgenin alanı : %0.2f "%alan)

ucgen=Ucgen()
ucgen.uzunlukGir()
ucgen.cevreHesapla()
ucgen.alanHesapla()