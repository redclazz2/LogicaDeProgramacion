#Explicación del Código y declaración de variables
print("En este programa se leen una cantidad determinada de nombres para devolver su longitud.")
A = int(input("Ingresa la cantidad de personas a contar: "))
B,C = [],[]
#Por cada i en un rango de 0 a la longitud expresada anteriormente, se añade el nombre a una lista
#y despues la longitud a otra
for i in range (0,A):
 B.append(input(f"Ingresa el nombre de la persona {i+1}: "))
 C.append(len(B[i]))
#Finalmente se imprimen ambas listas
print("Los nombres ingresados son:",B)
print("La longitud de cada nombre es:",C)
