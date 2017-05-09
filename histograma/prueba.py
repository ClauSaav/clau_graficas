from statistics import mean
import matplotlib.pyplot as plt
from matplotlib.pylab import hist, show

dato1 = [1395.5, 1382.5, 1379.0, 1258.0, 1228.5]
dato2 = [1395.5, 1382.5, 1379.0, 1258.0, 1228.5, 1083.5, 1050.0, 1015.5, 990.5, 956.5, 953.5, 949.5, 932.0, 922.5, 907.5, 899.5, 897.5, 881.0, 878.5, 844.0]

hist(dato1, color="black")
plt.xlabel('Peliculas', color="orange")
plt.ylabel('Rating', color="orange")
plt.title('Histograma TOP', color="red")
plt.tight_layout()
plt.savefig("histograma.png")
plt.show()

hist(dato2, color = "black")
plt.xlabel('Peliculas', color="orange")
plt.ylabel('Rating', color="orange")
plt.title('Histograma TOP', color="red")
plt.tight_layout()
plt.savefig("histograma2.png")
plt.show()

