segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos/3600
horasFin = horas//1
minutos = (horas-horasFin)*60
minutosEnt= minutos//1
segundos = (minutos-minutosEnt)*60
print("{0}:{1}:{2}".format(int(horasFin),int(minutosEnt),segundos))