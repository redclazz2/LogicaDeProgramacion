segundos = float(input("Ingrese la cantidad de segundos: "))
minutos = segundos/60
minutosFin = minutos//1
segundosTemp = minutos - minutosFin
segundosTemp = segundosTemp*60
print("Los minutos son:",minutos,"con",segundosTemp,"segundos")