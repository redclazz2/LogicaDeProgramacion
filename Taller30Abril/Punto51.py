i = 0
sumPar = 0
sumIpar = 0
n = int(input("Ingrese la cantidad de números a leer: "))
while i<n:
    numero = float(input("Ingrese un número para la sumatoria: "))
    if numero !=0:
        if numero % 2 == 0:
            sumPar += numero
        else:
            sumIpar += numero
    i+=1
promPar= sumPar / n
promIpar = sumIpar /n
print("La sumatoria de los numeros pares es:",promPar,"de los impares:",promIpar)