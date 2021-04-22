print("Este programa imprime los resultados de un polinomio de segundo grado.")
a = float(input("Ingrese el número a: "))
b = float(input("Ingrese el número b: "))
c = float(input("Ingrese el número c: "))
disc = (b**2) - (4*a*c)
if disc >= 0:
    x1 = (-b + (disc)**0.5) / (2*a)
    x2 = (-b - (disc) ** 0.5) / (2 * a)
    print("X1 = {0} X2 = {1}".format(x1,x2))
else:
    imaginario = ((-1*disc)**0.5)/ (2*a)
    real= (-1*b)/ (2*a)
    print(real,"+",imaginario,"i")
