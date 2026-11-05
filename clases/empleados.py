class Empleado(object):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_pago(self):
        return self.salario
    
    def descripcion(self):
        return f"{self.nombre}: ${self.calcular_pago():,.2f}"
    
class Vendedor(Empleado):
    def __init__(self, nombre, salario, ventas, comision=.05):
        super().__init__(nombre, salario)
        self.ventas = ventas
        self.comision = comision

    def calcular_pago(self):
        return super().calcular_pago() + self.comision * self.ventas
    


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre, salario=0)
        self.horas_trabajadas = horas
        self.tarifa = tarifa

    def calcular_pago(self):
        return self.horas_trabajadas * self.tarifa
    

