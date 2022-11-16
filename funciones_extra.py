import DataCleaning
import pandas as pd
import numpy as np
import matplotlib.pyplot as ptl
from scipy.stats import shapiro
from scipy import stats
def media_mes():
    datos =DataCleaning.main()
    datos2 = datos.groupby('first_observation_date').agg({
        'absolute_magnitude_h':'mean'
    })
    datos2.reset_index(inplace=True)
    print(datos2)
media_mes()
