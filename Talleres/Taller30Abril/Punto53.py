countMayor, countMenor, c = 0, 0, True
while (c == True):
    numero = int(input("Ingrese un número entero, ingrese 100 para terminar el programa: "))
    if numero > 100:
        countMayor += 1
    elif numero < 100:
        countMenor += 1
    elif numero == 100:
        c = False
print("La cantidad de números mayores a 100 fueron: {0} \nLa cantidad de números menores a 100 fueron: {1}".format(countMayor,countMenor))