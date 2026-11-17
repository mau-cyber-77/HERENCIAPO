
class Operacion:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calcular(self):
        return self.num1 + self.num2

    def mostrarResultado(self):
        resultado = self.calcular()
        print(f"Resultado de la operación: {resultado}")

class Resta(Operacion):
    def calcular(self):
        return self.num1 - self.num2


