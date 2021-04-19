#Esta función se encarga de retornar la sumatoria de los digitos introducidos
def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

cantidadSumatoriaMenora10 = 0
mayor = -1
n_mayorsuma = 0
numero = int(input("Ingrese un número positivo,ingrese -1 para terminar: "))
while numero >= 0:  #Cuando el número sea mayor a 0
    suma = sumaDigitos(numero)  #Se llama a  la función sumaDigitos
    if suma > mayor:            #Si el resultado anterior es mayor a los que ya se han registrado (en el primer ciclo siempre se reemplaza),
        mayor = suma            #se cambia como el mayor.
        n_mayorsuma = numero    #Se añade como el número con mayor suma de digitos el recien introducido por el usuario
    if suma < 10:               #Se verifica que la suma sea menor a 10 para sumar 1 y contar los números cuya sumatoria es menor a 10.
        cantidadSumatoriaMenora10 += 1
    numero = int(input("Ingrese un número positivo,ingrese -1 para terminar: "))
#Cuando se romple el bucle introduciendo -1, se imprime lo siguiente:
print("Sumatoria de dígitos del mayor número introducido fue:", n_mayorsuma, ":", mayor)
print("Cantidad de números introducidos con sumatoria de sus digitos menor a 10:", cantidadSumatoriaMenora10)

