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

class Test_Rectangulo(unittest.TestCase):
    def test_get_area(self):
        c1 = Rectangulo(4, 6)
        area = c1.get_area()
        self.assertEqual(area, 24)
    def test_get_perimetro(self):
        c1 = Rectangulo(4, 6)
        perimetro = c1.get_perimetro()
        self.assertEqual(perimetro, 20)

class Prueba_Rectangulo(Rectangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    def get_area(self):
        area = self.base * self.altura
        return area
    def get_perimetro(self):
        perimetro = self.base * 2 + self.altura * 2
        return perimetro

class Test_Prueba_Rectangulo(unittest.TestCase):
    def test_get_area(self):
        c1 = Prueba_Rectangulo(3,4)
        area = c1.get_area()
        self.assertEqual(area, 12)
    def  test_get_perimetro(self):
        c1 = Prueba_Rectangulo(3,4)
        perimetro = c1.get_perimetro()
        self.assertEqual(perimetro, 14)

rectangulo = Rectangulo(4,6)
rectangulo_1 = Prueba_Rectangulo(3,4)
print('El primer rectangulo tiene como perimetro : ', rectangulo.get_perimetro(), 'y como área : ', rectangulo.get_area())
print('El segundo rectangulo tiene como perimetro: ', rectangulo_1.get_perimetro(), 'y como área: ', rectangulo_1.get_area())

if __name__ == '__main__':
    unittest.main()
