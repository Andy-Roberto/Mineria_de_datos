import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
from scipy.stats import shapiro
from scipy import stats
def guardar(data_frame:pd.DataFrame):
    data_frame.to_csv("./base_de_datos_limpieza/NASA Near-Earth Objects_clean.csv")
def main() -> pd.DataFrame:
    datos = pd.read_csv('./base_de_datos_limpieza/NASA Near-Earth Objects_clean.csv',index_col=0,header=0)
    datos = datos[datos['kilometers_estimated_diameter_max'].isnull()==False]
    datos.drop(columns='name_limited')
    retorno:pd.DataFrame =fechas_desconosidas_omitir(datos,2)#1 Retorna fechas mes,dia y año donde se conozcan los 3, #2 Retorna el año #3 Retorna el año y mes
    # ptl.hist(retorno['absolute_magnitude_h'])
    # ptl.show()
    # print(retorno['first_observation_date'])
    retorno =quitar_nulos(retorno)
    # datos_norm_box , lambda_calc = stats.boxcox(retorno['absolute_magnitude_h'])
    # ptl.hist((normalizacion(retorno))['absolute_magnitude_h'],color='red',ec='black')
    # ptl.show()
    # print(retorno.isnull().sum())
    # guardar(retorno)
    return retorno
def quitar_nulos(data_frame:pd.DataFrame):
    datos = data_frame[data_frame['absolute_magnitude_h'].isnull()==False]
    return datos
def histograma(frame_data:pd.DataFrame,variable:str):
    ptl.hist((normalizacion(frame_data,variable))[variable],color='red',ec='black')
    ptl.show()
def omision(fechas:str,opcion):
    
    if(opcion==1):
        if("?" in fechas):
                return True;
        else:
            return fechas
    elif(opcion==2):
        if("?" in fechas.split('-')[0]):
                return True;
        else:
            return fechas.split('-')[0]
    else:
        if("?" in fechas):
                return True;
        else:
            return fechas.split('-')[0]+'-'+fechas.split('-')[1]
def fechas_desconosidas_omitir(datos: pd.DataFrame,opt):
    datos['first_observation_date'] = datos['first_observation_date'].apply(omision,args=[opt])
    datos_aux = datos[datos['first_observation_date']!=True]
    return datos_aux
def normalizacion(retorno:pd.DataFrame,variable:str):
    retorno[variable] = (retorno[variable]-retorno[variable].mean())/(retorno[variable].std())
    return retorno

main()