import pandas as pd
import numpy as np
datos = pd.read_csv('NASA Near-Earth Objects.csv',header=0)
datos2 = pd.read_table('NASA Near-Earth Objects.csv',header=0)
datos3 = pd.DataFrame(datos2)
print(datos)
print("\n")
print(datos2)
print("\n")
print(datos3)
print(datos2.dropna(axis='columns'))#No muestra la informacion de la columna que tenga almenos un Nan
print(datos['absolute_magnitude_h'].describe())
print(datos[['id','name','absolute_magnitude_h']].sort_values(by='absolute_magnitude_h'))#Ordena los valores
print(datos.groupby(['orbit_class_type']).size().reset_index(name="Cantidad de asteroides por tipo"))#Agrupa por la columna que selecciones, lo demas es para calcular la cantidad
def funcion(entrada):
    if entrada == True:
        return('Es peligroso')
    if entrada == False:
        return('No es peligroso')
print("Siguiente\n")
print(datos['is_potentially_hazardous_asteroid'].apply(funcion))
print("Siguiente\n")
datos.rename(columns={'name':'nombre'},inplace=True)
print(datos['nombre'])
print(datos.set_index('absolute_magnitude_h'))#Cambia el indice
datos.to_csv('nuevo_archivo.csv',index=False)
print(pd.read_csv('nuevo_archivo.csv',header=0))
print('head\n')
print(datos.head(3))
print('tail\n')
print(datos.tail(4))
print('info\n')
print(datos.info())
print('mean\n')
print(datos[['kilometers_estimated_diameter_max','absolute_magnitude_h']].apply(np.mean))
print('min\n')
print(datos[['kilometers_estimated_diameter_max','absolute_magnitude_h']].apply(np.min))
print('max\n')
print(datos[['kilometers_estimated_diameter_max','absolute_magnitude_h']].apply(np.max))

print('mean\n')
print(datos[['kilometers_estimated_diameter_max','absolute_magnitude_h']].mean())
print('count\n')
print(datos[['kilometers_estimated_diameter_max','absolute_magnitude_h']].count())
print('count\n')
print(datos[['kilometers_estimated_diameter_max','absolute_magnitude_h']].corr())
print('std\n')
print(datos[['kilometers_estimated_diameter_max','absolute_magnitude_h']].std())

print(datos.groupby(['orbit_class_type']).size())
print("////////////////////")
print(datos.groupby(['orbit_class_type'])[['is_potentially_hazardous_asteroid']].sum())
print("////////////////////")
datos10 = datos[datos['orbit_class_type']=='IEO']
print(datos10[['orbit_class_type','is_potentially_hazardous_asteroid']])
print(datos10.groupby(['is_potentially_hazardous_asteroid']).count())
print("////////////////////")
print(datos.groupby(['orbit_class_type'])[['is_potentially_hazardous_asteroid']].count())
