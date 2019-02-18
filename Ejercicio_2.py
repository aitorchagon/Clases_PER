import unittest
class Contador():
    def __init__ (self, x = None):
        self.x = x
        if x is None:
            self.x = 30
    def ascension(self):
        return self.x + 1
    def descenso(self):
        return self.x - 1
cohete = Contador(20)
print("El cohete está en la posición con respecto al suelo:", cohete.ascension())

class Test_Contador(unittest.TestCase):
    def test_ascension(self):
        c1 = Contador(20)
        ascenso = c1.ascension()
        self.assertEqual(ascenso, 21)
    def test_descenso(self):
        c1 = Contador(20)
        descender = c1.descenso()
        self.assertEqual(descender, 19)

if __name__ == '__main__':
    unittest.main()
