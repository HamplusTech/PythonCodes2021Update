import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,6,1)
y = np.linspace(1,5,5)
z = np.logspace(1,2,5)

plt.plot(x,y,"-or")
plt.plot(x,z,"-*g")
plt.xlabel("Natural Number")
plt.ylabel("Linear & Log Space")
plt.legend(["Linear Space", "Log Space"])

plt.show()
