numero = input("Ingrese un número entero menor a 100000 para calcular la cantidad de dígitos que tiene: ")
if int(numero)<100000:
    print("El número tiene:",len(numero),"digitos.")
else:
    print("El número es mayor a 100000, la entrada es inválida.")