print("Ejercicio 5 y 6")

frase = input("Ingrese una frase corta para hacer el listado de las vocales, solo incluir letras minusculas sin simbolos especiales ni tildes...")
longitudFrase = len(frase)

arrayVocales = ["a","e","i","o","u"]
arrayEncontradas = []

for x in range(0,longitudFrase):
    for i in range(0,len(arrayVocales)):
        if (frase[x].lower() == arrayVocales[i]) and frase[x].lower() not in arrayEncontradas:
                arrayEncontradas.append(frase[x].lower())

print("Vocales encontradas:", arrayEncontradas)