velocidad = float(input("Ingrese la velocidad del objeto (m/s): "))
tiempo = float(input("Ingrese el tiempo del movimiento (s): "))
aceleracion = float(input("Ingrese la aceleración del objeto(m/s**2): "))
distancia = velocidad * tiempo + 1/2 * 10 * tiempo ** 2
print("La distancia recorrida en el movimiento fue:",distancia,"m")