def calcular_aporte_sindical(edad, sueldo):
    aporte = 0

    if edad <= 30:
        aporte = sueldo * 0.02
    else:
        if sueldo <= 20000:
            aporte = sueldo * 0.01
        elif sueldo <= 50000:
            aporte = sueldo * 0.02
        else:
            aporte = sueldo * 0.03

    return aporte

edad = int(input("Ingrese la edad del empleado: "))
sueldo = float(input("Ingrese el sueldo anual en dólares: "))


aporte_sindical = calcular_aporte_sindical(edad, sueldo)

if edad <= 30:
    aporte_sindical *= 1.2


print(f"El monto del aporte sindical es: {aporte_sindical} dólares")
