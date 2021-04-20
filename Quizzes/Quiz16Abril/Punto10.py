def caracteres(string:str):
    x = string.split()
    return x[-1]

inputString = input("Ingrese una oración para hallar la longitud en caracteres de la palabra final: ")
e = caracteres(inputString)
print("La longitud de la última palabra es:",len(e))
