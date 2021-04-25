palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")
palabraLista = list(palabra.lower())
palabraInver = list(palabra.lower())
palabraInver.reverse()
if palabraLista == palabraInver:
    print("Es un palíndromo!")
else:
    print("No es un palíndromo!")


