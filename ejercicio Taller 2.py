import numpy as np

mu=3
sigma=0.5
n=2000
vals=np.random.normal(loc=mu, scale=sigma, size=n)
vals2=n*sigma
print(vals)
print(vals2)

#Histograma de datos generados
import matplotlib.pyplot as plt
count, bins, ignored=plt.hist(x=vals, bins=30)
plt.title("histograma de tiempos de servicio")
plt.xlabel("Tiempos de servicio")
plt.ylabel("Frecuencia")
plt.show()

print(count)