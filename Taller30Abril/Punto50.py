i = 0
sum = 0
n = int(input("Ingrese la cantidad de números a leer: "))
while i<n:
    numero = float(input("Ingrese un número para la sumatoria: "))
    sum += numero
    i+=1
prom= sum / n
print("La sumatoria es:",prom)