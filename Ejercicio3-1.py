import numpy as np
import matplotlib.pyplot as plt

h, lx, o= .01, [np.arange(-5,5.2,0.2), np.arange(-5,5.2,0.2), np.arange(-2*(np.pi),2*(np.pi),1/4), np.arange(1,10.18,0.18)], 0
f, axs = plt.subplots(2,2)
def graph(i, j, x, y1, y2, o):
        axs[i,j].plot(x, y1, '.')
        axs[i,j].plot(x, y2, '--')
        ly=[]
        for k in range(0,len(y1)):
                if y1[k]==y2[k]:
                        ly.append(y1[k])
        print("\n\nLos valores de la función " + str(o+1) + " es: \n" + str(y1)+ "\n\n y: \n"+ str(y2))
        axs[i,j].grid(True)

def funciones(i, j, lx, o):
        if o==0:
                y1=np.exp(lx)
                y2=(np.exp(lx+h)-np.exp(lx-h))/(2*h)
                graph(i,j,lx,y1,y2,o)
        elif o==1:
                y1=-4*np.exp(-2*np.power(lx,2))*lx
                y2=(np.exp(-2*np.power(lx+h,2))-np.exp(-2*np.power(lx-h,2)))/(2*h)
                graph(i,j,lx,y1,y2,o)
        elif o==2:
                y1= (-1*np.sin(lx))
                y2= (np.cos(lx+h)-np.cos(lx-h))/(2*h)
                graph(i,j,lx,y1,y2,o)
        elif o==3:
                y1= 1/lx
                y2= (np.log(lx+h)-np.log(lx-h))/(2*h)
                graph(i,j,lx,y1,y2,o)

for i in range(0,2):
        for j in range(0,2):
                if i==0:
                        funciones(i, j, lx[i+j], o)
                else:
                        funciones(i, j, lx[i+j+1], o)
                o+=1

plt.show()
