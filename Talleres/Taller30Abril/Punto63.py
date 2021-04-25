palabra = input()
lista = list(palabra)
listaMayus = list(palabra.upper())
mayusculas,minusculas = 0,0
for i in range(len(lista)):
    if lista[i]==listaMayus[i]:
        mayusculas +=1
    else:
        minusculas +=1
if mayusculas==minusculas:
    print(palabra.lower())
elif mayusculas>minusculas:
    print(palabra.upper())
else:
    print(palabra.lower())