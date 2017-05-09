import numpy as numpy
import matplotlib.pyplot as plt
import csv
import pandas as pd
from matplotlib.pylab import hist, show

prueba= pd.read_csv("/home/administradorcito/gra34/pruebas/movies/final.csv")
#print(prueba.head())
#print(prueba.describe())
#print("Rating",prueba['rating'].describe())
ratings = prueba[['rating','title','user_id']]
#print(ratings.head())
mostrar= ratings.groupby(['title','rating']).sum()
print("\n",mostrar.unstack().head())
histograma = mostrar.unstack().plot(kind='bar',stacked=True ,figsize=(9,7))
histograma.set_title("Interaccion de Rating por usuario", color='blue')
histograma.set_ylabel("Rango de Interaccion", color='red')
histograma.set_xlabel("Películas",fontsize=10, color ='red')
histograma.legend(["0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0"],title='Rating', loc=1, ncol=1)
plt.tight_layout()
plt.savefig("histXinterac.png")
