#Introducción, se explica la función del programa, se pide el tamaño de la lista y el número a utilizar
print("Este programa llena una lista con los múltiplos del número ingresado, el usuario determina el tamaño de la lista:")
n = int(input("Ingrese el tamaño de la lista (Número Entero): "))
m = int(input(f"Ingrese el número del que se calcularan {n} múltiplos: "))
a = []
#Por cada i en rango de 1 a el tamaño de la lista + 1
for i in range (1,n+1):
    #Por medio de la función append se añade el múltiplo a la lista
    a.append(i*m)
#Finalmente se imprime la lista
print (f"Los múltiplos de {m} son: ",a)
