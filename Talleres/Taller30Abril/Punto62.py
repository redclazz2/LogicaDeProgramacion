palabra = input()
lista = list(palabra)
lista.pop(0)
palabra=palabra.upper()
listaMayus = list(palabra)
print(listaMayus[0],end="")
i=0
while i<len(lista):
   print(lista[i],end="")
   i+=1