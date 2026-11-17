"""
ACTIVIDAD 1

1. ¿Cuál es el nombre de la clase? producto
2. ¿Cuáles son sus propiedades? nombre, precio
3. ¿Cuáles son sus métodos? calcularTotal
4. ¿Qué función cumple __init__? Inicializa las propiedades del objeto
5. ¿Para qué se utiliza self? Para referirse a la instancia actual del objeto
6. ¿En qué instrucción se crea un objeto? producto1 = Producto("Cuaderno", 35.0)
7. ¿Cuál es el nombre del objeto? producto1
8. ¿Cómo se llama a calcularTotal()? producto1.calcularTotal(3)
9. ¿Qué valores recibe el constructor cuando se crea el objeto? "Cuaderno", 35.0
10. ¿Qué resultado mostrará el programa? 105.0

"""



"""
Actividad 2
"""
class Rectangulo(object):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def mostrarArea(self):
        print("El área del rectángulo es:", self.calcularArea())


"""
Actividad 3

1. ¿Cuál es la clase padre?  Operacion
2. ¿Cuál es la clase hija?  Multiplicacion
3. ¿Cómo se indica la herencia?  Con la sintaxis de paréntesis en la definición de la clase hija: class Multiplicacion(Operacion):
4. ¿Qué propiedades utiliza la clase hija? numero1 y numero2
5. ¿Por qué puede utilizarlas sin definir su propio __init__?  Porque hereda el __init__ de la clase padre
6. ¿Por qué los métodos calcular() tienen resultados distintos?  Porque están redefiniendo el método en la clase hija para realizar una operación diferente
7. ¿Qué valores se imprimen?  12 y 32
8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?  Se utilizaría el método calcular() de la clase padre, que suma los dos números.
"""