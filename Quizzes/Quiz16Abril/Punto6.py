def factorial(cant):
    numero = int(input("Ingrese un número para encontrar su factorial (-1 o 0 para terminar): "))
    f = 1
    if numero != 0 and numero != -1:
        for i in range(1, numero + 1):
            f = f * i
        print("Factorial de {0} es {1}:".format(numero,f))
        cant += 1
        factorial(cant)
    elif numero == -1 or numero == 0:
        print("Se leyeron un total de",cant,"numeros")


factorial(0)

