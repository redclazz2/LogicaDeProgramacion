def division():
    try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            div = num1/num2
            print("El resultado es: ",div)
    except:
        print("Madre mía, Willy, una entrada no es válida o intentaste dividir por 0!")
        division()

division()