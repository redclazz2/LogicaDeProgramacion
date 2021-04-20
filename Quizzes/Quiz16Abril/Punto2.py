def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma


num = int(input("Número a procesar, ingrese 0 para terminar el programa: "))
while num != 0:
    print("La suma de los dígitos del número ingresado es:", sumaDigitos(num))
    num = int(input("Número a procesar, ingrese 0 para terminar el programa: "))
else:
    print("Operación terminada con éxito!")

