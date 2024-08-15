import numpy as np

mu=4
sigma=0.5
n=1000
vals=np.random.normal(loc=mu, scale=sigma, size=n)
vals2=n*sigma
print(vals)
print(vals2)