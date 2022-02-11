# import matplotlib.pyplot as plt
# import numpy as np

x, y, sigma = np.loadtxt("sinusoidPlot .txt", unpack=True)

theta = np.linspace(0, 2*np.pi,1000) # Create 1000 equally spaced points between 0 and 2*pi
plt.xlabel("$x$ (m)")
plt.ylabel("$y$ (m/s)")
plt.errorbar(x,y,yerr = sigma,fmt = ".")
plt.plot(theta,3*np.sin(theta))
plt.fig("plotExcersise.pdf")
