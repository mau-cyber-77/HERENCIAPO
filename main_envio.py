from clases.paqueteria import Envio, EnvioExpress, EnvioSobre

def main():
    # Crear instancias de envíos
    envio1 = Envio("Carlos López", 5)  # 5 kg
    envio2 = EnvioSobre("María Fernández")  # Sobre
    envio3 = EnvioExpress("Pedro Sánchez", 3)  # 3 kg con envío express

    # Lista de envíos
    envios = [envio1, envio2, envio3]

    # Mostrar resumen y costo de cada envío
    for envio in envios:
        print(envio.resumen())  


if __name__ == "__main__":
    main()