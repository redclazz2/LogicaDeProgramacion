def programMain():
    num1 = int(input("Ingrese el primer número natural: "))
    num2 = int(input("Ingrese el segundo número natural: "))

    if num2>num1:
        for i in range(num1,num2+1):
            print(i)
    else:
        print("Entradas no válidas")
        programMain()
programMain()