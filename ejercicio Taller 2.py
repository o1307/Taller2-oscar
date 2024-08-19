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

from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Normal (mu=0, sigma=1)
x= np.arange(-4,4,0.001)
plt.plot(x, norm.pdf(x))
plt.title('Función de densidad normal estándar')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.show()
