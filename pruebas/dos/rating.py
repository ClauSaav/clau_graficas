import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pydataset import data
from matplotlib.pylab import hist, show

# parametros esteticos de seaborn
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
final = pd.read_csv('/home/administradorcito/gra34/pruebas/dos/final.csv')
final.head()

#FRECUENCIA
frecuencia = (pd.value_counts(final['title']))
print(frecuencia)
#r = (pd.value_counts(final['rating']))
#print(r)

final['rating'].hist(bins=5, color='orange', normed=1, histtype='barstacked', rwidth=0.8)

plt.title("Histograma de Peliculas", color='red')
plt.xlabel("Rango de Rating", color='blue')
plt.ylabel("Frecuencia", color='blue')
plt.legend()
plt.savefig("histprueba.png")
plt.show()


#frec = frecuencia.to_dict()
#print(frecuencia)
#name = frecuencia[''].keys()
#print(name)#grafica
#frecuencia.hist(bins=5)
#plt.xlabel("Evaluación de Rating")
#plt.ylabel("Frecuencia")
