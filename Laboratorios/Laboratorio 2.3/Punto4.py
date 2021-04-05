entrada = 0
ArrayNumeros = []
i = True
while(i):
    entrada = input("Ingrese un número real para añadir a una lista, ingrese FIN para terminar: ")
    if entrada != "FIN":
        entrada = float(entrada)
        ArrayNumeros.append(entrada)
    elif entrada == "FIN":
        i = False
ArrayNumeros.sort()
print("Se ingresaron un total de {0} números, que son los siguientes: \n{1}".format(len(ArrayNumeros),ArrayNumeros))