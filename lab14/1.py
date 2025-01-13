import numpy as np
import matplotlib.pyplot as plt
import csv

x1 = np.linspace(1,10, 50)
y1 = (1/x1)*np.cos(x1**2+1/x1)
plt.plot(x1,y1,label="Y(x)=(1/x)*cos(x^2+1/x)",color="green",linewidth=7)
plt.title("my plt",fontsize=10)
plt.xlabel("x",fontsize=10, color="black")
plt.ylabel("y",fontsize=10, color="black")
plt.legend()
plt.grid(True)
plt.savefig("plot.png",dpi=300)
