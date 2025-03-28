class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        else:
            return "Está sobre el origen"
        
    def vector(self, vector2):
        return (self.x - vector2.x, self.y - vector2.y)
    
    def distancia(self, vector2):
        return ((self.x - vector2.x) ** 2 + (self.y - vector2.y) ** 2) ** 0.5