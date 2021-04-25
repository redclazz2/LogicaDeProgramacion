palabras=[]
n = int(input())
for i in range(0,n):
    palabras.append(input())
for palabra in palabras:
    if len(palabra)>10:
        lista = list(palabra)
        print(f"{lista[0]}{len(lista)-2}{lista[len(lista)-1]}")
    else:
        print(palabra)