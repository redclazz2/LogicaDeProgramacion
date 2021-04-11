print("Ejercicio 8")
año1 = int(input("Ingrese el primer año: "))
año2 = int(input("Ingrese el segundo año: "))

if año1 > año2:
    print("Entrada no valida, terminando la ejecución.")

for x in range(año1,año2+1):
    if x % 4 == 0 and (x % 100 != 0 or x % 400 == 0) and x %10 ==0:
         print("Es bisiesto y multiplo de 10:",x)

