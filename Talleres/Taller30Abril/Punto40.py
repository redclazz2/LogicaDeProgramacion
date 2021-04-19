lista=["","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
def programaMain():
    n = int(input("Ingrese el número del día que se desea consultar: "))
    if 0<n<8:
        print("El día es:",lista[n])
    else:
        print("entrada no válida.")
        programaMain()

programaMain()