import numpy as np
import matplotlib.pyplot as plt

listax, listay = [],[]
media,desviación = [0.5, 1, 1.5, 2, 0.5, 1, 1.5, 2], [1, 2, 3, 4, 4, 3, 2, 1]
np.set_printoptions(precision=2)
listax = np.arange(-10,10.4,0.4)
f, axs = plt.subplots(4,4)

for i in range(0,4):
    for j in range(0,4):
        m = media[i+j]
        s = desviación[i+j] 
        listay = (1/np.power((2*(np.pi*180)*s),1/2))*np.exp((-1/2)*np.power((listax-m)/s,2))
        axs[i,j].plot(listax,listay)
        print("Valores de media: " + str(m) + " y desviacion: " + str(s) + ":")
        print(str(listay))
        axs[i,j].grid(True)
        listay = np.delete(listay,50)

plt.show()