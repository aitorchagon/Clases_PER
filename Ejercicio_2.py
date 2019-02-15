import unittest
class Contador():
    def __init__ (self,x):
        self.x = x
    def ascension(self):
        return self.x + 1
    def descenso (self):
        return self.x - 1
cohete = Contador(20)
print("El cohete está en la posición con respecto al suelo:", cohete.ascension())

class Test_Contador(unittest.TestCase):
    def test_ascension(self):
        c1 = Contador(2)
        ascenso = c1.ascension()
        self.assertEqual(ascenso, 2)
    def test_descenso(self):
        c1 = Contador(3)
        descender = c1.descenso(3)
        self.assertEqual(descenso, 3)

class Contador_1():
    def __init__ (self, valor = None):
        self.valor = valor
        if valor is  None:
            self.valor = 26
        else:
            return self.valor
    def ascension(self):
        return self.valor + 1
    def descenso(self):
        return self.valor -1
cohete = Contador_1()
print("El cohete está en la posición:", cohete.descenso())

class Test_Contador_1(unittest.TestCase):
    def test_ascension(self):
        c1 = Contador_1(3)
        ascenso = c1.ascension
        self.assertEqual(ascension, 4)
    def test_descender(self):
        c1 = Contador_1(4)
        descender = c1.descenso
        self.assertEqual(descenso, 3)
