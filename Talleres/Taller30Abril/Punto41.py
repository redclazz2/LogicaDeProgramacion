n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

if n1 == n2 or n2 == n3 or n1 == n3:
    print("Al menos dos son iguales!")
else:
    print("Ningun número es igual!")