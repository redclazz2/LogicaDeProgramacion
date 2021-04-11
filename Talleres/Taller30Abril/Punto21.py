final = 0
numero = int(input("Ingrese el número positivo y entero: "))
while (numero > 0):
    digitoAlmacenar = numero % 10
    final = (final * 10) + digitoAlmacenar
    numero = numero // 10
print("El número de manera inversa es: {}".format(final))