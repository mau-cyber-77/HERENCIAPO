from ejercicios.ejercicio_2_estacionamiento import Estancia, EstanciaPension, EstanciaNocturna

def main():
    estancia = Estancia("Carlos", 3)
    estancia_pension = EstanciaPension("Ana")
    estancia_nocturna = EstanciaNocturna("Luis", 5)

    estancias = [estancia, estancia_pension, estancia_nocturna]

    for e in estancias:
        print(e.ticket())

if __name__ == "__main__":
    main()

