import numpy as np
array = np.array([[1,2,3,4],[5,6,7,8],[5,6,7,8]],dtype=np.int64)
print(array)

unos = np.ones((3,4))
print(unos)

ceros = np.zeros((3,4))
print(ceros)

aleatorios = np.random.random((2,2))
print(aleatorios)

vacía = np.empty((3,2))
print(vacía)

full = np.full((2,2),8)
print(full)

espacio1 = np.arange(0,30,5)
print(espacio1)
espacio2 = np.linspace(0,2,5)
print(espacio2)

# Crear una matriz identidad
identidad1 = np.eye(4,4)
print(identidad1)
identidad2 = np.identity(4)
print(identidad2)

#Consultar longspace