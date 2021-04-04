num1 = float(input("Ingrese un número decimal: "))

if num1>0:
    parteEntera = num1 // 1
    parteDecimal = num1 - parteEntera
else:
    parteEntera = num1 // -1
    parteDecimal = (num1 + parteEntera) * -1
    print("El número es negativo!")

print(parteDecimal,parteEntera)
input("Presione cualquier tecla para terminar...")