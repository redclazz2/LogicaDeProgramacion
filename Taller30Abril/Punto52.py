def programaMain():
    try:
        num = int(input("Ingrese un número entero positivo:"))
        if num > 0:
            print(num)
        else:
            print("Entrada no válida.")
            programaMain()
    except:
        print("entrada no válida.")
        programaMain()

programaMain()