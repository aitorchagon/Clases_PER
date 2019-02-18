import unittest
class Libro:
    def __init__ (self,paginas, titulo, genero, fechafinal, periodoprestamo):
        self.paginas = paginas
        self.titulo = titulo
        self.genero = genero
        self.fechafinal = fechafinal
        self.periodoprestamo = periodoprestamo
    def dame_info(self, paginas, titulo, genero):
        informacion = []
        informacion.append(self.paginas)
        informacion.append(self.titulo)
        informacion.append(self.genero)
        return informacion
    def prestamo(self, periodoprestamo = None):
        if periodoprestamo is None:
            self.periodoprestamo = '15 días'
        return periodoprestamo
harrypotter = Libro(345, 'Harry Potter', 'fantasia', 27, None)
informacion_libro = harrypotter.dame_info(345, 'Harry Potter', 'fantasia')
prestamo_libro = harrypotter.prestamo('15 días')
print('El libro cuyas páginas, título y género respectivamente son : ', informacion_libro, 'será prestado durante : ', prestamo_libro)
class Test_libro (unittest.TestCase):
    c1 = Libro(345, 'Harry Potter', 'fantasia', 27, None)
    def dame_info_test(self):
        self.assertEqual(c1.informacion, informacion)
    def prestamo_test(self):
        self.assertEqual(c1.prestamo, '15 días' )
if __name__ == '__main__':
    unittest.main()

    
