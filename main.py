from clases.empleados import Empleado, Vendedor, EmpleadoPorHoras

def main():
    # Crear instancias de empleados
    empleado1 = Empleado("Juan Pérez", 3000)
    vendedor1 = Vendedor("Ana Gómez", 2500, ventas=10000)
    empleado_horas1 = EmpleadoPorHoras("Luis Martínez", horas=40, tarifa=15)

    # Lista de empleados
    empleados = [empleado1, vendedor1, empleado_horas1]

    # Mostrar descripción y pago de cada empleado
    for empleado in empleados:
        print(empleado.descripcion())


if __name__ == "__main__":
    main()