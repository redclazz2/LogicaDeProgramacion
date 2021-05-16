import pandas as pd
def aprobados(notas):
    notas = pd.Series(notas)
    print("nota minima",notas.min(),'\nNota maxima',notas.max(),'\nPromedio',notas.mean(),'\nDesviacion Estandar',notas.std())

notas = {'Juan':5, 'Maria':4.5, 'Pedro':2, 'Carmen': 4.5, 'Luis':5}
aprobados(notas)