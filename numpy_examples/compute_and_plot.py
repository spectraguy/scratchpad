import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 100)
y = np.random.normal(size=x.shape)

# Average a rectangular window of up to 21 samples
yavg = np.zeros(shape=x.shape)
for i in range(yavg.size):
    imin = max(i - 10, 0)
    imax = min(i + 10, yavg.size)
    yavg[i] = np.mean(y[imin:imax])

# Apply a Gaussian kernel with 7-sample standard deviation
kernel = np.exp(-np.power(np.arange(-14, 15) / 7, 2))
kernel /= np.sum(kernel)
yconv = np.convolve(y, kernel, mode='same')

plt.title("Demo sample averaging")
plt.xlabel("Sample")
plt.ylabel("Value")
data_line, = plt.plot(x, y)
avg_line, = plt.plot(x, yavg)
conv_line, = plt.plot(x, yconv)
plt.legend([data_line, avg_line, conv_line], ['Data', 'Rectangular window avg', 'Gaussian smoothing'])
plt.show()
