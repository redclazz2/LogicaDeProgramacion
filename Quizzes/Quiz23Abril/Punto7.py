participantes, decision,podio,ronda,i = [], 0,[],1,0
try:
    cantidad = int(input("Ingrese la cantidad de participantes del torneo (Número Entero): "))

    while i < cantidad:
        nombre = input(f"Ingrese el nombre del participante {i + 1}: ")
        yaRegistrado = participantes.count(nombre)
        if yaRegistrado > 0:
            print("Ya se registró un jugador con el mismo nombre!")
            participantes.clear()
            i = 0
            continue
        elif yaRegistrado == 0:
            participantes.append(nombre)
            i += 1
    print("Se ha registrado a:", participantes)
    total = len(participantes)

    while (len(participantes) > 1):
        eliminar = input(f"Ronda {ronda}, ingrese el jugador eliminado: ")
        if participantes.index(eliminar) > -1:
            podio.append(eliminar)
            participantes.remove(eliminar)
            ronda += 1

    podio.append(participantes[0])
    for r in range(len(podio), 0, -1):
        print(f"Puesto {r}: {podio[-r]}")
    print(f"El ganador es: \n{podio[-1]} \nFelicitaciones!")
except ValueError:
    print("Error!, posiblemente ingresó un dato no válido o intentó eliminar un jugador no registrado!")