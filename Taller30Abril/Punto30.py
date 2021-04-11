ArrayNumeros = []
i = 0
while i<3:
    numero = float(input("Ingrese un número: "))
    ArrayNumeros.append(numero)
    i+=1
ArrayNumeros.sort()
print("El menor número introducido es: {0} y el mayor: {1}".format(ArrayNumeros[0],ArrayNumeros[2]))