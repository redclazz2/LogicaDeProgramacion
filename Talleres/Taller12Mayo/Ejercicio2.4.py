import pandas as pd
datos = {'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500,35600,28300,33900],'Gastos':[22000,23400,18100,20700]}
datos = pd.DataFrame(datos)
print(datos)