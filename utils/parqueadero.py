class Parqueadero:
    def __init__(self, cupos_carros, cupos_motos):
        self.cupos_carros = cupos_carros
        self.cupos_motos = cupos_motos
        self.disponibles_carros = cupos_carros
        self.disponibles_motos = cupos_motos
        

    def ingresar_vehiculo(self, tipo, entrada_salida):
        if tipo == "carro" and entrada_salida == "Entrada" and self.disponibles_carros > 0:
            self.disponibles_carros -= 1
            return f"Carro ingresado. La tarifa por hora es $3500. Cupos disponibles: {self.disponibles_carros} carros."
        elif tipo == "moto" and entrada_salida == "Entrada" and self.disponibles_motos > 0:
            self.disponibles_motos -= 1
            return f"Moto ingresada. La tarif apor hora es $2000. Cupos disponibles: {self.disponibles_motos} motos."
        elif tipo == "moto" and entrada_salida == "Salida":
            self.disponibles_motos += 1
            return f"Moto saliendo. Cupos disponibles: {self.disponibles_motos} motos."
        elif tipo == "carro" and entrada_salida == "Salida":
            self.disponibles_carros += 1
            return f"Carro saliendo. Cupos disponibles: {self.disponibles_carros} carros."
        elif tipo == "carro":
            return "No hay cupos disponibles para carros."
        elif tipo == "moto":
            return "No hay cupos disponibles para motos."
        else:
            return "Tipo de vehículo no válido."

    def liberar_cupo(self, tipo):
        if tipo == "carro" and self.disponibles_carros < self.cupos_carros:
            self.disponibles_carros += 1
            return f"Cupo de carro liberado. Cupos disponibles: {self.disponibles_carros} carros."
        elif tipo == "moto" and self.disponibles_motos < self.cupos_motos:
            self.disponibles_motos += 1
            return f"Cupo de moto liberado. Cupos disponibles: {self.disponibles_motos} motos."
        else:
            return "No hay cupos ocupados para liberar."
