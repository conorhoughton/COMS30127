import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10)
plt.plot(x, np.sin(x), linewidth=2,label="sine")
plt.plot(x, np.cos(x), linewidth=2,label="cosine")

plt.legend()


plt.xlabel("x")
plt.ylabel("y")
plt.title("an example plot")
plt.savefig("example.png")
plt.show()




