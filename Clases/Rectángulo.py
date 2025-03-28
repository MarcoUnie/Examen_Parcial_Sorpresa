class Rectangulo:
    def __init__(self, puntoi, puntof):
        self.puntoi = puntoi
        self.puntof = puntof

    def base(self):
        return abs(self.puntoi[0] - self.puntof[0])

    def altura(self):
        return abs(self.puntoi[1] - self.puntof[1])
    
    def area(self):
        return self.base() * self.altura()