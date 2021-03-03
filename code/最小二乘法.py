import numpy as np
import matplotlib.pyplot as plt

# 1
x = np.arange(0, 10, 0.2)
yi = [5 * i + 3 for i in x]
y = [np.random.normal(yi, 2) for yi in yi]
# plt.plot(x,y,colar="red",linewidth=1)
plt.scatter(x, y, c="c")
plt.show()

# 2
x_bar = np.mean(x)
y_bar = np.mean(y)

x_sum = 0
y_sum = 0

for i in range(len(x)):