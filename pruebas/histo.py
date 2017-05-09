import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pydataset import data
from matplotlib.pylab import hist, show

#parametros esteticos de seaborn
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
final = pd.read_csv('/home/administradorcito/gra34/pruebas/movies/final.csv')
final.head()


#rating = final[['rating','title','user_id']]
#print(rating.head())
#mostrar = rating.groupby(['title','rating']).sum()
#print("\n",mostrar.unstack().head())
#FRECUENCIA
frecuencia = (pd.value_counts(final['title']))
print(final)

final['rating'].hist(bins=5, color='orange', normed=1, histtype='barstacked', rwidth=0.8)


plt.title("Histograma de Peliculas", color='red')
plt.xlabel("Rango de Rating", color='blue')
plt.ylabel("Frecuencia", color='blue')
plt.legend()
plt.savefig("histprueba.png")
plt.show()



