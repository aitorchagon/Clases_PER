import unittest

class Complejo(object):
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def sumar(self, otro):
        result = Complejo(self.real + otro.real,
                            self.imag + otro.imag)
        return result

    def restar(self, otro):
        result = Complejo(self.real - otro.real,
                            self.imag - otro.imag)
        return result

    def multiplicar(self, otro):
        resultado = Complejo(self.real * otro.real, self.imag * otro.imag)
        return resultado

    def dividir(self, otro):
        resultad_real = Complejo(((self.real * otro.real)/(otro.real ** 2 + otro.imag ** 2))
        resultad_complejo = Complejo(((self.imag * otro.real - self.real * otro.imag)/ (otro.real ** 2 + otro.imag ** 2)))
        resultad = (resultad_real, resultad_complejo)
        return resultad

    def igual(self, otro):
        return self.real == otro.real and self.imag == otro.imag


class TestComplejo(unittest.TestCase):

    def test_sumar(self):

        c1 = Complejo(1,2)
        c2 = Complejo(3,4)

        suma = c1.sumar(c2)

        self.assertEqual(suma.real, 4)
        self.assertEqual(suma.imag, 6)

    def test_restar(self):

        c1 = Complejo(6,1)
        c2 = Complejo(8,4)

        restar = c1.restar(c2)

        self.assertEqual(restar.real, -2)
        self.assertEqual(restar.imag, -3)

    def test_multiplicar(self):
        c1 = Complejo(5,4)
        c2 = Complejo(7,2)

        multiplicar = c1.multiplicar(c2)

        self.assertEqual(multiplicar.real, 35)
        self.assertEqual(multiplicar.imag, 8)

    def test_dividir(self):
        c1 = Complejo(2,3)
        c2 = Complejo(1,9)
        dividir = c1.dividir(c2)
        self.assertEqual(dividir.real, )
        self.assertEqual(dividir.imag, 1/45)

if __name__ == "__main__":
    unittest.main()
