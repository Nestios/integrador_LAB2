def realizar_operacion(numero1, numero2, operador):
    resultado = 0

    if operador == '+':
        resultado = numero1 + numero2
    elif operador == '-':
        resultado = numero1 - numero2
    elif operador == 'x':
        resultado = numero1 * numero2
    elif operador == '/':
        resultado = numero1 / numero2
    return resultado

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
operador = input("Ingrese el símbolo de la operación (+, -, x, /): ")
if operador in ['+', '-', 'x', '/']:
    resultado = realizar_operacion(numero1, numero2, operador)
    print(f"El resultado de la operación es: {resultado}")
else:
    print("Error: Operador inválido.")
