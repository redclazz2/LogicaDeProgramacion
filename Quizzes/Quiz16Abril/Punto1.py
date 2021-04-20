def validar():
    direccion = input("Para validar el email, este debe contener @, de otra manera saldrá error \nTu email: ")
    if direccion.find("@")<0:
        print("Dirección no válida, debe contener @")
        validar()
    else:
        print("Dirección de correo válida")

validar()