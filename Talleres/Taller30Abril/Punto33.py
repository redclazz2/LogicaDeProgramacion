año = int(input("Ingrese el año a evaluar: "))
if not año % 4 and (año % 100 or  not año % 400):
    print("Es bisiesto")
else:
    print("No es bisiesto")
