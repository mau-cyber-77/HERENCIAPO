"""
Un estacionamiento cobra por hora según la duración total de la estancia: 
Horas 
Tarifa por hora 
1 a 2 --- $15.00 
3 a 5 --- $12.00 
Más de 5 --- $10.00 
La tarifa del rango correspondiente se aplica a TODAS las horas registradas. 
• Crear la clase Estacionamiento. Su constructor __init__ recibe horas y las guarda como propiedad. 
• Crear calcularPago() para devolver el importe total calculado con if/elif/else. 
• Crear mostrarRecibo() que utilice calcularPago() y muestre horas e importe con dos decimales. 
• En el programa principal, solicitar las horas, comprobar que sea un entero mayor que cero, crear un objeto y 
llamar a mostrarRecibo(). 

"""


class Estacionamiento:
    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):
        if 1 <= self.horas <= 2:
            return self.horas * 15.00
        elif 3 <= self.horas <= 5:
            return self.horas * 12.00
        elif self.horas > 5:
            return self.horas * 10.00
        else:
            return 0.00

    def mostrarRecibo(self):
        pago = self.calcularPago()
        print(f"Horas: {self.horas}, Importe: ${pago:.2f}")


def main():
    while True:
        try:
            horas = int(input("Ingrese la cantidad de horas (entero mayor que cero): "))
            if horas > 0:
                break
            else:
                print("Por favor, ingrese un número mayor que cero.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    estacionamiento = Estacionamiento(horas)
    estacionamiento.mostrarRecibo()


if __name__ == "__main__":
    main()
