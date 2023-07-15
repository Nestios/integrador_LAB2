def calcular_precio_terreno(ancho, largo, precio_metro_cuadrado):
    area = ancho * largo
    precio_terreno = area * precio_metro_cuadrado
    return precio_terreno

def calcular_metros_alambre(ancho, largo):
    perimetro = (ancho + largo) * 2
    metros_alambre = perimetro * 3
    return metros_alambre


ancho = float(input("Ingrese el ancho del terreno en metros: "))
largo = float(input("Ingrese el largo del terreno en metros: "))
precio_metro_cuadrado = float(input("Ingrese el precio del metro cuadrado de tierra: "))
precio_terreno = calcular_precio_terreno(ancho, largo, precio_metro_cuadrado)
metros_alambre = calcular_metros_alambre(ancho, largo)
print(f"El precio del terreno es: USD {precio_terreno}")
print(f"La cantidad de metros de alambre necesarios es: {metros_alambre} metros")
