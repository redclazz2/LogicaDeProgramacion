import math
def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def factorial(numero):
    f = math.factorial(numero)
    return f

def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

def digitoFrecuencia(numero :str):
    digito = input("Ingrese un solo dígito para verificar cuantas veces aparece en la cadena: ")
    if len(digito) == 1:
        if numero.count(digito) > 0:
            print("El", digito, "aparece",numero.count(digito), "veces")
        else:
            print("El digito no aparece en el número.")
    else:
        print("El digito no es válido!")
        digitoFrecuencia(numero)
mayor = 0
numero = int(input("Ingrese un número primo, ingrese uno que no lo sea para terminar la ejecución: "))
while primo(numero):
    print("Suma de los dígitos del número:", sumaDigitos(numero))
    digitoFrecuencia(str(numero))
    if numero > mayor:
        mayor = numero
    numero = int(input("Ingrese un número primo, ingrese uno que no lo sea para terminar la ejecución: "))
print("Factorial del número más grande introducido", mayor, "es:", factorial(mayor))

