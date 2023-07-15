def mostrar_tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un número entero entre 1 y 10: "))
if numero >= 1 and numero <= 10:
    mostrar_tabla_multiplicar(numero)
else:
    print("Error: El número ingresado está fuera del rango válido.")
