import numpy as np
import matplotlib.pyplot as plt

h, lx12, lx3, lx4= .01, np.arange(-5,5.2,0.2), np.arange(-2*(np.pi*360),2*(np.pi*360)), np.arange(1,10.18,0.18)

f, axs = plt.subplots(2,2)

ly1= np.exp(lx12)
ly2= (np.exp(lx12+h)-np.exp(lx12-h))/(2*h)
axs[0,0].plot()
