class ClimaDiario:
    def __init__(self, temperatura):
        self.temperatura = temperatura

    def obtener_temperatura(self):
        return self.temperatura

class PromedioSemanal:
    def __init__(self):
        self.dias = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            clima = ClimaDiario(temp)
            self.dias.append(clima)

    def calcular_promedio(self):
        total_temperaturas = sum([clima.obtener_temperatura() for clima in self.dias])
        return total_temperaturas / len(self.dias)

# Función principal que organiza el flujo del programa
def main():
    print("Bienvenido al programa de promedio semanal del clima.")
    promedio_semanal = PromedioSemanal()
    promedio_semanal.ingresar_temperaturas()
    promedio = promedio_semanal.calcular_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
