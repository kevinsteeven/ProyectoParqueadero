import unittest
from utils.parqueadero import Parqueadero
class testParqueadero(unittest.TestCase):

    def setUp(self): #inicializar instancia de parqueadero con 10 cupos para carro y 10 para moto
        self.parqueadero = Parqueadero(10, 10)

    def test_ingresar_carro(self): #Prueba de ingreso de caroo con cupos disponibles
        resultado = self.parqueadero.ingresar_vehiculo("carro", "Entrada")
        self.assertEqual(resultado, "Carro ingresado. Cupos disponibles: 9 carros.")
        self.assertEqual(self.parqueadero.disponibles_carros, 9)

    def test_ingresar_moto(self): #Prueba de ingreso de moto con cupos disponibles
        resultado = self.parqueadero.ingresar_vehiculo("moto", "Entrada")
        self.assertEqual(resultado, "Moto ingresada. Cupos disponibles: 9 motos.")
        self.assertEqual(self.parqueadero.disponibles_motos, 9)

    def test_salida_moto(self):#Prueba de salida de moto
        self.parqueadero.ingresar_vehiculo("moto", "Entrada")
        resultado = self.parqueadero.ingresar_vehiculo("moto", "Salida")
        self.assertEqual(resultado, "Moto saliendo. Cupos disponibles: 10 motos.")
        self.assertEqual(self.parqueadero.disponibles_motos, 10)

    def test_salida_carro(self):#Prueba de salida de carro
        self.parqueadero.ingresar_vehiculo("carro", "Entrada")
        resultado = self.parqueadero.ingresar_vehiculo("carro", "Salida")
        self.assertEqual(resultado, "Carro saliendo. Cupos disponibles: 10 carros.")
        self.assertEqual(self.parqueadero.disponibles_carros, 10)

    def test_liberar_cupo_carro(self):  # Prueba de liberacion de cupo manual para carro
        self.parqueadero.ingresar_vehiculo("carro", "Entrada")
        resultado = self.parqueadero.liberar_cupo("carro")
        self.assertEqual(resultado, "Cupo de carro liberado. Cupos disponibles: 10 carros.")
        self.assertEqual(self.parqueadero.disponibles_carros, 10)

    def test_liberar_cupo_moto(self): # Prueba de liberacion de cupo manual para moto
        self.parqueadero.ingresar_vehiculo("moto", "Entrada")
        resultado = self.parqueadero.liberar_cupo("moto")
        self.assertEqual(resultado, "Cupo de moto liberado. Cupos disponibles: 10 motos.")
        self.assertEqual(self.parqueadero.disponibles_motos, 10)

    def test_no_hay_cupos_carros(self): #Prueba de entrada de carro si no hay cupo
        self.parqueadero.disponibles_carros = 0
        resultado = self.parqueadero.ingresar_vehiculo("carro", "Entrada")
        self.assertEqual(resultado, "No hay cupos disponibles para carros.")

    def test_no_hay_cupos_motos(self): #Prueba de entrada de moto si no hay cupo
        self.parqueadero.disponibles_motos = 0
        resultado = self.parqueadero.ingresar_vehiculo("moto", "Entrada")
        self.assertEqual(resultado, "No hay cupos disponibles para motos.")



