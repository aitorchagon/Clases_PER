import unittest
class Cuenta:
    def __init__(self, ingreso, reintegrar, transferir):
        self.ingreso = ingreso
        self.reintegrar = reintegrar
        self.transferir = transferir
    def informacion (self):
        return self.ingreso, self.reintegro, self.transferencia
    def almacenar_informacion(self):
        caja = []
        caja.append(self.ingreso)
        caja.append(self.reintegro)
        caja.append(self.transferencia)
        return caja
class TestCuenta(unittest.TestCase):
    def test_informacion (self):
        c1 = Cuenta(30, 40, 80)
        informaciones = c1.informacion()
        self.assertEqual(informacion.ingreso, 30)
        self.assertEqual(informacion.reintegro, 40)
        self.assertEqual(informacion.transferencia, 80)
        

banco = Cuenta(4999,43,789)
print('Se ha observado en mi cuenta un ingreso de:', banco.ingreso, 'un reintegro de:', banco.reintegrar, 'y una transferencia de: ', banco.transferir)
print('En la actualidad tengo', cuenta.informacion())
