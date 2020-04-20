class hayvanlarAlemi:
    def __init__(self):
        self.evcil=True
        self.memeli=True
    def memeliMi(self):
        if self.memeli:
            print("Memeli hayvan")
        else:
            print("Memeli bir hayvan değil")
    def evcilMi(self):
        if self.evcil:
            print("Evcil hayvan")

class kedi(hayvanlarAlemi):
    def __init__(self):
        super().__init__()
    def memeliMi(self):
        super().memeliMi()

class japonBaligi(hayvanlarAlemi):
    def __init__(self):
        super().__init__()
        self.memeli=False
        self.yuzebilir=True
    def memeliMi(self):
        super().memeliMi()
    def yuzebilirMi(self):
        if self.yuzebilirMi:
            print("Yüzebilir")

x = kedi()
x.memeliMi()
x.evcilMi()

j=japonBaligi()
j.yuzebilirMi()
j.memeliMi()