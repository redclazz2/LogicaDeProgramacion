dias = int(input("Ingrese el número de días de estadia: "))
distancia = float(input("Ingrese la distancia recorrida en el vuelo en KM: "))
costo = distancia * 5000
if costo < 100000:
    costo = 100000
if distancia > 1000 or dias > 7:
    costo = costo * 0.15

print("El costo del viaje es:",costo)