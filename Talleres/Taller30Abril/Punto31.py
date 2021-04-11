num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
sum = num1 + num2
if sum > num3:
    print("La suma entre {0} y {1} da {2} y es mayor a {3}".format(num1,num2,sum,num3))
else:
    print("La suma entre {0} y {1} da {2} y es menor a {3}".format(num1, num2,sum, num3))