import random
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("Sueldos asignados.")

def clasificar_sueldos():
    menores_800k = []
    entre_800k_y_2M = []
    superiores_2M = []
    
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            menores_800k.append((trabajador, sueldo))
        elif sueldo <= 2000000:
            entre_800k_y_2M.append((trabajador, sueldo))
        else:
            superiores_2M.append((trabajador, sueldo))

    total_sueldos = sum(sueldos)
    print("Sueldos menores a $800.000 TOTAL:", len(menores_800k))
    for empleado, sueldo in menores_800k:
        print(f"{empleado} ${sueldo}")
    print("\nSueldos entre $800.000 y $2.000.000 TOTAL:", len(entre_800k_y_2M))
    for empleado, sueldo in entre_800k_y_2M:
        print(f"{empleado} ${sueldo}")
    print("\nSueldos superiores a $2.000.000 TOTAL:", len(superiores_2M))
    for empleado, sueldo in superiores_2M:
        print(f"{empleado} ${sueldo}")
    print("\nTOTAL SUELDOS: $", total_sueldos)

def ver_estadisticas():
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    media_geom = math.exp(sum(math.log(s) for s in sueldos) / len(sueldos))
    print("--------------------------------") 
    print("Sueldo más alto:", sueldo_max)
    print("--------------------------------") 
    print("Sueldo más bajo:", sueldo_min)
    print("--------------------------------") 
    print("Promedio de sueldos:", promedio)
    print("--------------------------------") 
    print("Media geométrica:", media_geom)
    print("--------------------------------") 

def reporte_sueldos():
    print(f"{'Nombre empleado':<20} {'Sueldo Base':<15} {'Descuento Salud':<15} {'Descuento AFP':<15} {'Sueldo Líquido':<15}")
    for trabajador, sueldo in zip(trabajadores, sueldos):
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        print(f"{trabajador:<20} ${sueldo:<14} ${descuento_salud:<14.2f} ${descuento_afp:<14.2f} ${sueldo_liquido:<14.2f}")

def main():
    while True:
        print("\nMenú:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            asignar_sueldos_aleatorios()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_sueldos()
        elif opcion == "5":
            print("Finalizando programa…")
            print("Desarrollado por Danilo Celis")
            print("RUT 20.987.789-9")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
