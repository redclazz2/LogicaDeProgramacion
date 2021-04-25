datos = [4,5,9,10]
print("4.1:")
for i in range(0, 4):
    print(datos[i], end=" ")
print()
datos[2]=-10
print("4.2:")
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()
datos.insert(1, 11)
print("4.3:")
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()
datos.remove(5)
print("4.4:")
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()
datos = datos + [21, 22]
print("4.5:")
for i in range(0, len(datos)):
    print(datos[i], end=" ")
print()


