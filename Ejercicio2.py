import numpy as np
import matplotlib.pyplot as plt

lx = np.arange(-10,10.1,0.1)
a=int(input("Ingrese a:"))
b=int(input("Ingrese b:"))
c=int(input("Ingrese c:"))
ly=a*np.power(lx,2)+b*lx+c
plt.plot(lx,ly)
plt.title("Las raices son: " + str(np.roots([a,b,c])))
print("Los valores fueron los siguientes: \n" + str(ly))
plt.grid(True)
plt.show()