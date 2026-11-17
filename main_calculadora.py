from ejercicio2_examen.calculadora_con_herencia import Operacion, Resta

def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    suma = Operacion(num1, num2)
    resta = Resta(num1, num2)

    print("Operación de Suma:")
    suma.mostrarResultado()

    print("Operación de Resta:")
    resta.mostrarResultado()

if __name__ == "__main__":
    main()
