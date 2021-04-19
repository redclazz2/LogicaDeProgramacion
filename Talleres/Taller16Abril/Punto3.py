def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

sumatoria = 0
num = int(input("Número a procesar, ingrese 0 para terminar el programa: "))
while num != 0:
    print("Suma de los dígitos del número ingresado:", sumaDigitos(num))
    sumatoria = sumatoria + num
    num = int(input("Número a procesar, ingrese 0 para terminar el programa: "))
print("Sumatoria de los números ingresados:", sumatoria)
print("Sumatoria de los digitos del total de números ingresados:", sumaDigitos(sumatoria))

