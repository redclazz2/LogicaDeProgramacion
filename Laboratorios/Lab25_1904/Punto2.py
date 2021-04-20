def coordenadaZ(x, y):
    for i in range(3):
        x = x + 1
        y = y + 1
    return x , y
# programa principal
x = int(input("Ingrese la coordenada del eje x: "))
y = int(input("Ingrese la coordenada del eje y: "))
print("Coordenadas finales:",coordenadaZ(x,y))
