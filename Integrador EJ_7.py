def mostrar_sucesion_pares(numero):
    sucesion = ""

    for i in range(numero, -1, -2):
        sucesion += str(i) + " "
    return sucesion.strip()
numero = int(input("Ingrese un número entero positivo: "))
if numero >= 0:
    sucesion_pares = mostrar_sucesion_pares(numero)
    print(sucesion_pares)
else:
    print("Error: El número ingresado no es positivo.")
