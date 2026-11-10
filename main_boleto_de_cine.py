from ejercicios.ejercicio_1_boleto_de_cine import Boleto, BoletoEstudiante, BoletoCortesia, BoletoTerceraEdad


def main():
    boleto = Boleto("Carlos", "Sala 1, 18:00")
    boleto_estudiante = BoletoEstudiante("Ana", "Sala 2, 20:00")
    boleto_cortesia = BoletoCortesia("Luis", "Sala 3, 22:00")
    boleto_tercera_edad = BoletoTerceraEdad("Diana", "Sala 1, 16:00")

    boletos = [boleto, boleto_estudiante, boleto_cortesia, boleto_tercera_edad]
    
    for b in boletos:
        print(b.ticket())
  

if __name__ == "__main__":
    main()