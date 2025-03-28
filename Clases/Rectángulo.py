class Rectangulo:
    def __init__(self, puntoi, puntof):
        self.puntoi = puntoi
        self.puntof = puntof

    def base(self):
        return abs(self.puntoi[0] - self.puntof[0])
