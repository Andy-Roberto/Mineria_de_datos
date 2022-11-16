import DataCleaning
import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
from scipy.stats import shapiro
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
datos =DataCleaning.main()

datos2 = datos


# DataCleaning.histograma(datos,"absolute_magnitude_h")
def arrg(tipo:str):
    if((tipo=="aphelion_distance" or tipo=="perihelion_distance")):
        return [['min','max','mean','median',np.std,np.var,'skew',pd.Series.kurtosis],
                ['Minimo','Maximo','Media','Mediana','Desviacion estandar','Varianza','Asimetria','kurtosis']]
    else:
        return [['min','max','mean','median', pd.Series.mode,np.std,np.var,'skew',pd.Series.kurtosis],
                ['Minimo','Maximo','Media','Mediana','Moda','Desviacion estandar','Varianza','Asimetria','kurtosis']]
    
def tablas_peligrosos_(tipo:str):
    grupo =datos.groupby(['orbit_class_type','is_potentially_hazardous_asteroid']).agg({
        tipo: arrg(tipo)[0]
    })
    grupo.columns=arrg(tipo)[1]
    grupo.to_csv(f'./Analisis_de_Datos/Estadistica_descriptiva/Dangerous_{tipo}.csv',index=True)
def tablas_(tipo):
    grupo2 = datos.groupby(['orbit_class_type'])[[tipo]]
    grupo2.boxplot(figsize=(10,10))
    ptl.savefig(f"./Analisis_de_Datos/Graficas/{tipo}.jpg")
    grupo =datos.groupby('orbit_class_type').agg({
    tipo: arrg(tipo)[0]
    })
    grupo.columns=arrg(tipo)[1]
    grupo.to_csv(f'./Analisis_de_Datos/Estadistica_descriptiva/{tipo}.csv',index=True)

def principal():
    datos=['absolute_magnitude_h','kilometers_estimated_diameter_min','kilometers_estimated_diameter_max','aphelion_distance']
    datos=['absolute_magnitude_h']
    for tipo in datos:
        tablas_(tipo)
        tablas_peligrosos_(tipo)
    nova()
def nova():
    
    nuevo = ols("absolute_magnitude_h ~ orbit_class_type", data=datos).fit()
    anova_= sm.stats.anova_lm(nuevo, typ=2)
    if anova_["PR(>F)"][0] < 0.05:
        print("hay diferencias")
        print(anova_)
        
    else:
        
        print("No hay diferencias")
    datos.boxplot('absolute_magnitude_h',by='orbit_class_type')
    ptl.savefig("./Analisis_de_Datos/Anova/Grafica.jpg")
    ptl.show()
principal()
