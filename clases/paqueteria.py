class Envio(object):
    def __init__(self, destinatario, peso):
        self.destinatario = destinatario
        self.peso = peso

    def calcular_costo(self):
        return self.peso * 20 + 100

    def resumen(self):
        return f"Envio de {self.peso} kg a {self.destinatario}: ${self.calcular_costo():,.2f}"
    

class EnvioSobre(Envio):
    def __init__(self, destinatario):
        super().__init__(destinatario, peso=0)

    def calcular_costo(self):
        return 80


class EnvioExpress(Envio):
    def __init__(self, destinatario, peso, extra=0.6):
        super().__init__(destinatario, peso)
        self.extra = extra

    def calcular_costo(self):
        costo_normal = super().calcular_costo()
        return costo_normal * (1 + self.extra)
