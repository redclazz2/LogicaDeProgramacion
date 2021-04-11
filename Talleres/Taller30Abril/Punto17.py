segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos/3600
parteEntera = horas // 1
parteDecimal = horas - parteEntera
extra = parteDecimal * 60
print("La cantidad de horas es:",parteEntera,"con",round(extra),"minutos aprox.")