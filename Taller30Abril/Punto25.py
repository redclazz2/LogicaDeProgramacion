compra = float(input("Ingrese el valor de la compra: "))
iva = compra * 0.19
desc = 0
if compra >= 150000:
    desc = compra * 0.05
print("Valor original {0}, valor del iva {1}, compra + iva {2}, descuento {3}, valor con descuento {4}".format(compra,iva,compra + iva,desc,compra+iva-desc))