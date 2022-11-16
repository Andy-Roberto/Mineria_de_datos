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
from sklearn.cluster import KMeans
datos =DataCleaning.main()
datos = datos[['orbit_class_type','absolute_magnitude_h','kilometers_estimated_diameter_min','perihelion_distance','aphelion_distance']][0:1000]
# datos=datos.groupby('orbit_class_type')[['absolute_magnitude_h']]
IEO = datos[datos['orbit_class_type']=='IEO'][0:200]
APO = datos[datos['orbit_class_type']=='APO'][0:100]
AMO = datos[datos['orbit_class_type']=='AMO'][0:100]
ATE = datos[datos['orbit_class_type']=='ATE'][0:100]
# def escater():
#     plt.scatter(IEO['perihelion_distance'],IEO['aphelion_distance'],
#             marker="*",s=150,color='skyblue',label="Clase IEO")
#     plt.scatter(APO['perihelion_distance'],APO['aphelion_distance'],
#                 marker="*",s=150,color='red',label="Clase APO")
#     plt.scatter(AMO['perihelion_distance'],AMO['aphelion_distance'],
#                 marker="*",s=150,color='yellow',label="Clase AMO")
#     plt.scatter(ATE['perihelion_distance'],ATE['aphelion_distance'],
#                 marker="*",s=150,color='orange',label="Clase ATE")

def escalamiento():
    datos2 = datos[['perihelion_distance','aphelion_distance']]
    clase = datos['orbit_class_type']
    escalador = preprocessing.MinMaxScaler().fit(datos2.values)
    datos2 = pd.DataFrame(escalador.transform(datos2.values),columns=['perihelion_distance','aphelion_distance'])
    kmeans = KMeans(n_clusters=6).fit(datos2.values)
    datos2['cluster'] = kmeans.labels_
    plt.figure(figsize=(6,5),dpi=100)
    colors = ["blue","red","black","purple",'orange','yellow']
    print(kmeans.cluster_centers_,kmeans.inertia_)
    for cluster in range(kmeans.n_clusters):
        plt.scatter(datos2[datos2['cluster']==cluster]['perihelion_distance'],
            datos2[datos2['cluster']==cluster]['aphelion_distance'],marker='o',s=40,color=colors[cluster],alpha=0.5)
        plt.scatter(kmeans.cluster_centers_[cluster][0],
                kmeans.cluster_centers_[cluster][1],
                    marker="P",s=180,color=colors[cluster])
    plt.title("Objetos espaciales",fontsize=20)
    plt.xlabel("Distancia Perihelion")
    plt.ylabel("Distancia Perihelion")
    plt.text(.2,1,f"k={kmeans.n_clusters}",fontsize=15)
    plt.text(.2,.9,f"Inercia={kmeans.inertia_}",fontsize=15)
    plt.xlim(-0.1,1.1)
    plt.ylim(-0.1,1.1)
    plt.plot(scalex=500,scaley=500)
    plt.savefig("./Clustering/Clustering.jpg")
    plt.show()
def graficar(perihelion,aphelion,solicitante,clasificador):
    plt.ylabel('Aphelion Distance')
    plt.xlabel('Perihelion Distance')
    
    plt.scatter(perihelion,aphelion,marker="+",s=40,color="black",label=f"Dato Clase{clasificador.predict(solicitante)},Probabilidades por clase {clasificador.predict_proba(solicitante)}")
    plt.legend(loc='upper center')
    print("Clase",clasificador.predict(solicitante))
    print("Probabilidades por clase", clasificador.predict_proba(solicitante))
    
    
    
def main():
    # escater()
    escalamiento()
main()
# escalamiento()