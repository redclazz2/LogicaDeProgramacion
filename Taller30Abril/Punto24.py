numero = int(input("Ingrese un número entero que no sea 0: "))
if numero%2 == 0:
    texto1 = "Es par"
else:
    texto1 = "Es impar"

if numero > 0:
     texto2 = "Es positivo"
else:
     texto2 = "Es negativo"

print("El número es {0} y {1}.".format(texto1,texto2))