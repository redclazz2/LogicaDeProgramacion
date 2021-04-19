contador,arrayNumeros = 0,[]
numero = int(input("Ingrese el número para evaluar sus factores"))
for i in range(1,numero+1):
    if numero % i == 0:
        contador += 1
        arrayNumeros.append(i)
print("Se encontraron un total de: {0} factores, resaltando: {1}".format(contador,arrayNumeros))
