def calcular_porcentaje_mayores_edad(edades):
    total_personas = len(edades)
    contador_mayores_edad = 0
    for edad in edades:
        if edad >= 18:
            contador_mayores_edad += 1
    porcentaje_mayores_edad = (contador_mayores_edad / total_personas) * 100
    return porcentaje_mayores_edad

cantidad_personas = int(input("Ingrese la cantidad de personas: "))
edades = []
for i in range(cantidad_personas):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)

porcentaje_mayores_edad = calcular_porcentaje_mayores_edad(edades)
print(f"El porcentaje de personas mayores de edad es: {porcentaje_mayores_edad}%")
