usernameStored = "Sebastian"
passwordStored = "09123"

def entradaMetodo():
    username = input("Ingrese el Nombre de Usuario: ")
    password = input("Ingrese la contraseña: ")

    if username == usernameStored and passwordStored == password:
        print("inicio de sesión correcto!")
    else:
        print("Error!, revise los datos.")
        entradaMetodo()

entradaMetodo()