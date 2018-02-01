
import PyPlot; 
const plt = PyPlot

x = linspace(0,2*pi,1000); y = sin.(3 * x + 4 * cos.(2 * x));
plt.plot(x, y, color="red", linewidth=2.0, linestyle="--")
plt.title("A sinusoidally modulated sinusoid")
plt.show()
