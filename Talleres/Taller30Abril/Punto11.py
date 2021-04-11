valor1 = input("Ingrese el valor de la primera variable: ")
valor2 = input("Ingrese el valor de la segunda variable: ")
print("El valor de la primera variable es: {0},el valor de la segunda variable es: {1}".format(valor1,valor2))
tempvar = valor1
valor1=valor2
valor2 = tempvar
print("El valor de la primera variable despues del intercambio es: {0}, de la misma manera, \nel valor de la segunda variable es: {1}".format(valor1,valor2))