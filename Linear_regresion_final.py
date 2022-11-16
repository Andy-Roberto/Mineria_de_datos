import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from statsmodels.formula.api import ols
from tabulate import tabulate
import statsmodels.formula.api as smf
import DataCleaning
def regresion_lineal(x,y,cantidad):
    datos =DataCleaning.main()
    aux = datos[0:cantidad]
    aux =aux.sort_values(by=['first_observation_date'],ascending=True)
    aux2=aux.sort_values(by=['first_observation_date'],ascending=True)
    aux =aux.groupby('first_observation_date').agg({
            'absolute_magnitude_h':'mean'
        })
    aux.reset_index(inplace=True)
    aux=aux.assign(indice=[i for i in range(len(aux[x]))])
    insertar3  ='indice'
    modelo_lineal = smf.ols(formula= f'{y} ~ {insertar3}',data=aux).fit()
    periodo = modelo_lineal.predict(pd.DataFrame(aux[f'{insertar3}']))
    aux2.plot(kind='scatter',x=f'{x}',y=f'{y}')
    plt.plot(aux[f'{insertar3}'],periodo,c='red',linewidth=3,)
    plt.xticks(rotation=90)
    plt.show()
def main():
    x = 'first_observation_date'
    y = 'absolute_magnitude_h'
    cantidad = 12000
    regresion_lineal(x,y,cantidad)
main()