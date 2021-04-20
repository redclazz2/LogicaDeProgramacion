par,impar,total,contcin,c = 0,0,0,0,True
while c:
    n = int(input("Ingrese el número a evaluar, la ejecución termina una vez se junten 10 números pares o se repita 5 veinte veces: "))
    if n%2 ==0:
        par +=1
    else:
        impar+=1
        if n == 5:
            contcin += 1
    total += 1

    if par == 10 or contcin == 20:
        c = False
print(f"Se contaron un total de {total} números, de los cuales {par} son pares, {impar} son impares \nRepitiendo 5: {contcin} veces. ")