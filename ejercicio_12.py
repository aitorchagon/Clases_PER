import unittest
class Coche:
    def __init__(self,color,marca,modelo,caballosdevapor,puerta,matricula):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballosdevapor = caballosdevapor
        self.puerta = puerta
        self.matricula = matricula
    def get_informacion(self):
        informacion = []
        informacion.append(self.color)
        informacion.append(self.marca)
        informacion.append(self.modelo)
        informacion.append(self.caballosdevapor)
        informacion.append(self.puerta)
        informacion.append(self.matricula)
        return informacion

class Test_Coche(unittest.TestCase):
    def test_get_informacion(self):
        c1 = Coche('negro','Lamborghini','Pegaso','2500CV',4,'4043GBA')
        informacion = c1.get_informacion()
        self.assertEqual(informacion, ['negro','Lamborghini','Pegaso','2500CV',4,'4043GBA'])

class PruebaCoche(Coche):
    def __init__(self,color,marca,modelo,caballosdevapor,puerta,matricula,cambio_color = None):
        if cambio_color is None:
            cambio_color = 'amarillo'
        else:
            self.cambio_color = cambio_color
    def informacion_actualizada(self):
        c1 = Coche('negro','Lamborghini','Pegaso','2500CV',4,'4043GBA')
        informacion = c1.get_informacion()
        informacion.append(self.cambio_color)
        return informacion

class Test_Prueba_Coche(unittest.TestCase):
    def test_informacion_actualizada(self):
        c1 = PruebaCoche('negro','Lamborghini','Pegaso','2500CV',4,'4043GBA','amarillo')
        informacion = c1.informacion_actualizada()
        self.assertEqual(informacion, ['negro','Lamborghini','Pegaso','2500CV',4,'4043GBA', 'amarillo'])

lamborghini = Coche('negro','Lamborghini','Pegaso','2500CV',4,'4043GBA')
lamborghini_1 = PruebaCoche('negro','Lamborghini','Pegaso','2500CV',4,'4043GBA', 'amarillo')
print('Los datos del coche, ordenados según color inicial, marca, modelo, caballos de vapor, puertas y matricula son : ', lamborghini.get_informacion())
print('Los datos del coche, ordenados según color inicial, marca, modelo, caballos de vapor, puertas, matricula, y color final, son: ', lamborghini_1.informacion_actualizada())

if __name__ == '__main__' :
    unittest.main()
