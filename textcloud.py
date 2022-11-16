from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from statsmodels.formula.api import ols
from tabulate import tabulate
import statsmodels.formula.api as smf
import DataCleaning
def main():
    informacion =DataCleaning.main()
    texto = ""
    for parrafo in informacion["orbit_class_description"]:
        parrafo = parrafo.split('’')
        for frase in parrafo:
            if(len(frase)>1):
                texto = texto+" " + frase
    wc = WordCloud(max_font_size=60,mode="RGB",height=700,width=700).generate(texto)
    plt.imshow(wc,interpolation='bilinear')
    plt.axis("off")
    plt.savefig("./Webcloud/word_cloud.png")
main()
texto2 = "Hola como estás"
texto2 = texto2.split("á")
