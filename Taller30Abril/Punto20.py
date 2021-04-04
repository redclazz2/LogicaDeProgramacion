Cien,Cincuenta,Veinte,Diez,Cinco,Dos,Mil = 0,0,0,0,0,0,0
monto = float(input("Ingrese el monto: "))
restante = monto
while (restante>=100000):
    restante -= 100000
    Cien += 1
while (50000<=restante<100000):
    restante -= 50000
    Cincuenta += 1
while (20000<=restante<50000):
    restante -= 20000
    Veinte += 1
while (10000<=restante<20000):
    restante -=10000
    Diez += 1
while (5000<=restante<10000):
    restante -= 5000
    Cinco += 1
while (2000<=restante<5000):
    restante -= 2000
    Dos += 1
while (1000<=restante<2000):
    restante -= 1000
    Mil += 1

print("Para un monto de {0}, y un saldo restante de {1}, se pueden entregar: \nBilletes 100000: {2}\nBilletes 50000: {3} \nBilletes 20000: {4} \nBilletes 10000: {5} \nBilletes 5000: {6} \nBilletes 2000: {7} \nBilletes 1000: {8}".format(monto,restante,Cien,Cincuenta,Veinte,Diez,Cinco,Dos,Mil))

