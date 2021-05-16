import pandas as pd
inicio = int(input("Ingrese el año inicial: "))
fin = int(input("Ingrese el año final: "))
ventas = {}
for i in range(inicio,fin + 1):
     ventas[i]= float(input('Introduce las ventas del año ' + str(i) + ': ')) #Funciona de manera que i es el año y se le añade como valor
     #es lo mismo que tener ventas = {'2003':[X], 'XXXX':[XX]}
ventas = pd.Series(ventas)
print('Ventas \n',ventas)
print('Ventas con descuento\n',ventas*0.9)

# ventas = {'2003':[2], '2004':[5]}
# ventasDataFrame = pd.DataFrame(ventas)
# ventas = pd.Series(ventas)
# print(ventasDataFrame)
# print(ventas)

#El data frame hace que los valores en '' se vuelvan como el título, mientras que el series los pone como un valor dentro de la tabla.