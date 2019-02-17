import unittest
class Cuenta:
    def __init__(self, ingreso, reintegrar, transferir, total):
        self.ingreso = ingreso
        self.reintegrar = reintegrar
        self.transferir = transferir
        self.total = total
    def get_informacion(self):
        movimientos = []
        movimientos.append(self.ingreso)
        movimientos.append(self.reintegrar)
        movimientos.append(self.transferir)
        return movimientos
    def set_informacion(self, ingreso, reintegrar, transferir):
        caja = []
        caja.append(self.ingreso)
        caja.append(self.reintegrar)
        caja.append(self.transferir)
        caja.append(self.total)
        return caja
class TestCuenta(unittest.TestCase):
    def test_informacion (self):
        c1 = Cuenta(4999, 43, 789, 80000)
        informaciones = c1.get_informacion()
        self.assertEqual(c1.ingreso, 4999)
        self.assertEqual(c1.reintegrar, 43)
        self.assertEqual(c1.transferir, 789)
        self.assertEqual(c1.total, 80000)

if __name__ == '__main__':
    unittest.main()

banco = Cuenta(4999,43,789, 80000)
print('Se ha observado en mi cuenta un ingreso de:', banco.ingreso, 'un reintegro de:', banco.reintegrar, 'y una transferencia de: ', banco.transferir)
print('En la actualidad tengo', banco.get_informacion())
