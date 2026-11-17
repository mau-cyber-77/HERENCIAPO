

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


