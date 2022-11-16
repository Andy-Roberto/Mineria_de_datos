import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from statsmodels.formula.api import ols
from tabulate import tabulate
import statsmodels.formula.api as smf
import DataCleaning
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
datos =DataCleaning.main()
datos = datos[['orbit_class_type','absolute_magnitude_h','kilometers_estimated_diameter_min','perihelion_distance','aphelion_distance']]
# datos=datos.groupby('orbit_class_type')[['absolute_magnitude_h']]
IEO = datos[datos['orbit_class_type']=='IEO'][0:200]
APO = datos[datos['orbit_class_type']=='APO'][0:100]
AMO = datos[datos['orbit_class_type']=='AMO'][0:100]
ATE = datos[datos['orbit_class_type']=='ATE'][0:100]
def escater():
    plt.scatter(IEO['perihelion_distance'],IEO['aphelion_distance'],
            marker="o",s=150,color='skyblue',label="Clase IEO")
    plt.scatter(APO['perihelion_distance'],APO['aphelion_distance'],
                marker="*",s=150,color='red',label="Clase APO")
    plt.scatter(AMO['perihelion_distance'],AMO['aphelion_distance'],
                marker="v",s=150,color='yellow',label="Clase AMO")
    plt.scatter(ATE['perihelion_distance'],ATE['aphelion_distance'],
                marker="p",s=150,color='orange',label="Clase ATE")

def escalamiento():
    datos2 = datos[['perihelion_distance','aphelion_distance']]
    clase = datos['orbit_class_type']
    escalador = preprocessing.MinMaxScaler()
    datos2 = escalador.fit_transform(datos2.values)
    clasificador = KNeighborsClassifier(n_neighbors=3)
    clasificador.fit(datos2,clase.values)
    aphelion = 2.5
    perihelion = .35
    solicitante = escalador.transform([[perihelion,aphelion]])
    graficar(perihelion,aphelion,solicitante,clasificador)

def graficar(perihelion,aphelion,solicitante,clasificador):
    plt.ylabel('Aphelion Distance')
    plt.xlabel('Perihelion Distance')
    plt.scatter(perihelion,aphelion,marker="+",s=150,color="black",label=f"Dato Clase{clasificador.predict(solicitante)},Probabilidades por clase {clasificador.predict_proba(solicitante)}")
    plt.legend(loc='upper center')
    print("Clase",clasificador.predict(solicitante))
    print("Probabilidades por clase", clasificador.predict_proba(solicitante))
    plt.savefig("./Clasificacion/Classificacion.jpg")
    plt.show()
def main():
    escater()
    escalamiento()
main()
# escalamiento()


# datos.hist(edgecolor='red', linewidth=1.2)
# plt.show()
# datos.boxplot(by='orbit_class_type',figsize=(10,10))
