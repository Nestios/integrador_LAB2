from datetime import datetime

def calculo(fdn):
    hoy=datetime.datetime.now()
    edad=hoy.year-fdn.year
    if hoy.month<fdn.month or (hoy.month==fdn.month and hoy.day<fdn.day):
        edad -= 1
    return edad
def calculo2(fdn):
    hoy=datetime.now()
    proximo_cumple=datetime(hoy.year,fdn.month,fdn.day)
    if proximo_cumple<hoy:
        proximo_cumple=datetime(hoy.year+1,fdn.month,fdn.day)
    dias_faltantes=(proximo_cumple-hoy).days
    return dias_faltantes   
fdn_str=input("Ingresa tu fecha de nacimiento en el siguiente formato(DD/MM/AAAA):")
fdn= datetime.strptime(fdn_str, "%d/%m/%Y")
edad = calculo(fdn)
print(f"Tu edad Es:{edad}")

dias_faltantes=calculo2(fdn)
print(f"faltan {dias_faltantes} para tu proximo cumple.")