class Estancia(object):
    def __init__(self, placa, horas):
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores que cero")
        self.placa = placa
        self.horas = horas

    def cobrar(self):
        return self.horas * 20

    def ticket(self):
        cobro = self.cobrar()
        return f"{self.placa} ({self.horas} h): ${cobro:,.2f}"

class EstanciaPension(Estancia):
    def __init__(self, placa):
        super().__init__(placa, 24)

    def cobrar(self):
        return 250

class EstanciaNocturna(Estancia):
    def __init__(self, placa, horas):
        super().__init__(placa, horas)

    def cobrar(self):
        return super().cobrar() + 50