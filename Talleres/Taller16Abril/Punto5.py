def funcionContadora(numero: str,digito: str):
    cantidad = numero.count(digito)
    return cantidad

num = (input("Ingrese un número entero para evaluar las veces en que un digito aparece en él: "))
un_digito = (input("Ingrese el dígito a buscar: "))
print("Frecuencia del dígito en el número:", funcionContadora(num,un_digito))
