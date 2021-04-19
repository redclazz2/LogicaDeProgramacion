numero = int(input("Ingrese la el valor máximo del intervalo a imprimir: "))
for i in range(1,numero+1):
    if i % 2 == 0:
        print("-",i)
    else:
        print(i)
