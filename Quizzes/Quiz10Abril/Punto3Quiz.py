diasDeLaSemana = [0,"Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
dia = int(input("Ingrese un día de la semana de 1 a 7:"))
if dia == 6 or dia == 7:
    temp = "y es festivo."
else:
    temp ="."
print("El día es: {0} {1}".format(diasDeLaSemana[dia],temp))
