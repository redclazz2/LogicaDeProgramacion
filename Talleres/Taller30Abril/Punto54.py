w,n,mayor,menor,impar,par,mulocho = True,0,0,0,0,0,0
while w:
    n = int(input("Ingrese un número cualquiera tenga en cuenta que el 0 es para terminar el programa:"))
    if n>0:
        mayor+=1
    elif n==0:
        w = False
        break;
    else:
        menor+=1
    if n%2 == 0:
        par +=1
    else:
        impar+=1
    if (n*-1)%8 == 0:
        mulocho += 1

print(f"La cantidad de números positivos introducidos es: {mayor} \nLa cantidad de números negativos introducidos es: {menor} \nLa cantidad de números pares introducidos es: {par}"
      f"\nLa cantidad de números impares introducidos es: {impar} \nLa cantidad de números multiplos de 8 es: {mulocho}")