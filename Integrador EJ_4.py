def determinar_momento_dia(hora):
    if hora >= 0 and hora <= 5:
        return "Madrugada"
    elif hora >= 6 and hora <= 11:
        return "Mañana"
    elif hora >= 12 and hora <= 13:
        return "Mediodía"
    elif hora >= 14 and hora <= 19:
        return "Tarde"
    elif hora >= 20 and hora <= 23:
        return "Noche"
    else:
        return "Error: La hora ingresada no es válida."

hora = int(input("Ingrese la hora del día (entre 0 y 23): "))
momento_dia = determinar_momento_dia(hora)
print(momento_dia)