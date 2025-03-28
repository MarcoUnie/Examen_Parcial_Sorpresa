from Clases.Punto import punto
from Clases.Rectángulo import Rectangulo

print("El cuadrante del punto D es:", punto(0,0).cuadrante())
print("El cuadrante del punto B es:", punto(5,5).cuadrante())
print("El cuadrante del punto C es:", punto(-3,-1).cuadrante())

print("El vector A y B es:", punto(2,3).vector(punto(5,5)))
print("El vector B y A es:", punto(5,5).vector(punto(2,3)))

print("la distancia de A a B es:", punto(2,3).distancia(punto(5,5)))
print("la distancia de B a A es:", punto(5,5).distancia(punto(2,3)))

print("La máxima distancia es del punto B:", max(punto(2,3).distancia(punto(0,0)), punto(5,5).distancia(punto(0,0)), punto(-3,-1).distancia(punto(0,0))))

Rectangulo_real = Rectangulo((2,3), (5,5))

print("La altura del rectángulo es:", Rectangulo_real.altura(), "La base del rectángulo es:", Rectangulo_real.base(), "El área del rectángulo es:", Rectangulo_real.area()) 