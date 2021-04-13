#Creación de la lista
Lista1 = [3,1,2]

#Uso de la función Append, que permite añadir un valor al final de la lista
Lista1.append(4)
print(Lista1[3]) #Devuelve el cuatro, que al quedar en la última posición, puede ser accedido con el índice 3.

#Uso de la función sorted, en el primer ejemplo se imprime de mayor a menor, en el segundo se ordena de menor a mayor.
print(sorted(Lista1,reverse=True))
print(sorted(Lista1))

#Uso de la función bin, que convierte el primer dígito de la lista en un binario.
#En este caso es 3 ya que a pesar de que se usó la sorted para cambiar el orden de la lista,
#Esta nueva formación nunca fue asignada como tal.
print(bin(Lista1[0]))