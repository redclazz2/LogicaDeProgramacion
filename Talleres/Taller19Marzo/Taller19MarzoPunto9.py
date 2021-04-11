print("Punto 9")
numero1 = int(input("Ingrese un número entero positivo: "))

f = 1
if numero1 != 0:
    for x in range(1, numero1 + 1):
        f = f * x

print("El número factorial es: ", f)
