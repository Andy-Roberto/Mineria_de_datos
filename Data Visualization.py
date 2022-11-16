

import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
def tamano_max_objetos(dato:pd.DataFrame):
    a=pd.DataFrame(columns=['IEO'])
    aux=dato[dato['orbit_class_type']=='IEO']
    a=a.assign(IEO=aux['kilometers_estimated_diameter_max'].values)
    b=pd.DataFrame(columns=['APO'])
    aux2=dato[dato['orbit_class_type']=='APO']
    b=b.assign(APO=aux2['kilometers_estimated_diameter_max'].values)
    c=pd.DataFrame(columns=['AMO'])
    aux3=dato[dato['orbit_class_type']=='AMO']
    c=c.assign(AMO=aux3['kilometers_estimated_diameter_max'].values)
    d=pd.DataFrame(columns=['ATE'])
    aux4=dato[dato['orbit_class_type']=='ATE']
    d=d.assign(ATE=aux4['kilometers_estimated_diameter_max'].values)
    return [a.to_numpy().flatten(),b.to_numpy().flatten(),c.to_numpy().flatten(),d.to_numpy().flatten()]

def datos_con_fecha(dato:pd.DataFrame):
    aux = dato[['kilometers_estimated_diameter_max','first_observation_date']][0:8000]
    aux =aux.sort_values(by=['first_observation_date'],ascending=True)
    # ptl.plot(aux.first_observation_date,aux['kilometers_estimated_diameter_max'])
    fix, ax = ptl.subplots(figsize=(20,4))
    ax.plot(pd.to_datetime(aux.first_observation_date),aux['kilometers_estimated_diameter_max'])
    ptl.ylabel('kilometers_estimated_diameter_max')
    ptl.xticks(rotation=90)
    ptl.savefig("./Data_Visualization/Linea_del_tiempo.png")
    ptl.show()
def graficar(info):
    ptl.boxplot(info,labels=["IEO","APO","AMO","ATE"])
    ptl.savefig("./Data_Visualization/Cajas.jpg")
    ptl.show()
def main():
    datos = pd.read_csv('NASA Near-Earth Objects.csv',header=0)
    datos = datos[datos['kilometers_estimated_diameter_max'].isnull()==False]
    arreglo = tamano_max_objetos(datos)
    graficar(arreglo)
    datos_con_fecha(datos)
main()
