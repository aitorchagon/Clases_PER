import unittest
class Rectangulo():
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura
    def get_area(self):
        area = self.base * self.altura
        return area
    def get_perimetro(self):
        perimetro = self.base * 2 + self.altura * 2
        return perimetro

class Prueba_Rectangulo(unittest.TestCase):
    def test_get_area(self):
        c1 = Rectangulo(4, 6)
        area = c1.get_area()
        self.assertEqual(area, 24)
    def test_get_perimetro(self):
        c1 = Rectangulo(4, 6)
        perimetro = c1.get_perimetro()
        self.assertEqual(perimetro, 20)
class Cuadrado():
    def __init__(self, lado):
        self.lado = lado
    def get_area(self):
        area = self.lado ** 2
        return area
    def get_perimetro(self):
        perimetro = self.lado * 4
        return perimetro

class Prueba_Cuadrado(unittest.TestCase):
    def test_get_area(self):
        c1 = Cuadrado (8)
        area = c1.get_area()
        self.assertEqual(area, 64)
    def test_get_perimetro(self):
        c1 = Cuadrado(8)
        perimetro = c1.get_perimetro()
        self.assertEqual(perimetro, 32)

class Triangulo():
    #Triángulo equilátero.
    def __init__(self, base, altura, lado):
        self.base = base
        self.altura = altura
        self.lado = lado
    def get_area(self):
        area = (self.base * self.altura)/2
        return area
    def get_perimetro(self):
        perimetro = self.base + self.altura + self.lado
        return perimetro

class Test_Triangulo():
    def test_get_area(self):
        c1 = Triangulo(2,3,4)
        area = c1.get_area()
        self.assertEqual(area, 3)
    def test_get_perimetro(self):
        c1 = Triangulo (2,3,4)
        perimetro = c1.get_perimetro()
        self.assertEqual(perimetro, 9)

rectangulo = Rectangulo(4, 6)
cuadrado = Cuadrado (8)
triangulo = Triangulo(2,3,4)

print('El área del rectángulo es:', rectangulo.get_area(),'y el perímetro es :' ,rectangulo.get_perimetro())
print('El área del cuadrado es: ', cuadrado.get_area(), 'y el perímetro es :', cuadrado.get_perimetro())
print('El área del triángulo es: ', triangulo.get_area(), 'y el perímetro es :', triangulo.get_perimetro())

if __name__ == '__main__':
    unittest.main()
