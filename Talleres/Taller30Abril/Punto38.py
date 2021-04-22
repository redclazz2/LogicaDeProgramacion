print("Este programa imprime si los numeros ingresados presentan un orden creciente, decreciente o ninguno.")
a = float(input("Ingrese el número a: "))
b = float(input("Ingrese el número b: "))
c = float(input("Ingrese el número c: "))

if a<b<c:
    print("Orden Creciente!")
elif a>b>c:
    print("Orden Decreciente!")
else:
    print("No se presenta un orden!")