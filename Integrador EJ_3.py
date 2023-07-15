def contar_billetes(monto):
    billetes = [100, 50, 20, 10, 5, 2, 1]
    cantidad_billetes = [0] * len(billetes)

    for i, valor_billete in enumerate(billetes):
        cantidad_billetes[i] = monto // valor_billete
        monto %= valor_billete

    return cantidad_billetes
monto = int(input("Ingrese el monto en dólares: "))
cantidad_billetes = contar_billetes(monto)
billetes = [100, 50, 20, 10, 5, 2, 1]
for i, cantidad in enumerate(cantidad_billetes):
    if cantidad > 0:
        print(f"{cantidad} billete(s) de US$ {billetes[i]}")
