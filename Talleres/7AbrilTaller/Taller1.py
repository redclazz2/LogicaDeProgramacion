while True:
    opcion = input("elige una fruta para tu desayuno:\n1.Manzanas\n2.Bananas\n3.Nada\n")

    if opcion == "1":
        print("Has seleccionado manzanas")
        break;
    elif opcion == "2":
        print("Has seleccionado bananas")
        break;
    elif opcion == "3":
        print("Has seleccionado nada")
        break;
    else:
        print("Debes seleccionar una opción (1,2 o 3)")

print("Programa terminado, que disfrutes de tu desayuno")

#En este ejercicio, la instrucción break se utiliza para romper el bucle una vez el usuario seleccione alguna opción del menú, de otra manera
#Se repite el bucle ya que no hay sentencia para salir.