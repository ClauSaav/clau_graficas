import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import seaborn as sns 
from pydataset import data
from matplotlib.pylab import hist, show

# parametros esteticos de seaborn
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
final = pd.read_csv('/home/administradorcito/gra34/histograma/movies/final.csv')
final.head()



#FRECUENCIA
frecuencia = (list(pd.value_counts(final['title'])))
print(frecuencia)

#final['rating'].hist(bins=5, color='pink')
#plt.xlabel("Evaluación de Rating")
#plt.ylabel("Frecuencia")
#plt.legend()
#plt.savefig("pruebasa.png")
#plt.show()
