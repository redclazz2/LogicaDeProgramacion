while True:
    opcion = input("elige una fruta para tu desayuno:\n1.Manzanas\n2.Bananas\n3.Nada\n")

    if opcion == "1":
        print("Has seleccionado manzanas")
        continue
    elif opcion == "2":
        print("Has seleccionado bananas")
        continue
    elif opcion == "3":
        print("Has seleccionado nada")
        continue
    else:
        print("Debes seleccionar una opción (1,2 o 3)")

print("Programa terminado, que disfrutes de tu desayuno")

#El programa a diferencia del otro, no tiene un fin, ya que no hay ningun punto en que el bucle se rompa
#Por tanto cada vez que se seleccione una de las 3 opciones o alguna fuera del menú, el codigo siempre
#regresará al inicio del bucle

