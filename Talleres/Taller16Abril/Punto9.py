def verificadorCedula(cedula :str):
    if len(cedula) == 8 or len(cedula)==10:
        print("La cedula es válida pues tiene 8 o 10 dígitos.")
    else:
        print("La cedula no es válida!")
inputCedula = input("Ingrese el número de la cedula para verificar que sea válida: ")
verificadorCedula(inputCedula)