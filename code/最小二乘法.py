import numpy as np
import matplotlib.pyplot as plt

# 1
x = np.arange(0, 10, 0.2)
y_ = [5 * i + 3 for i in x]
y = [np.random.normal(y_, 2) for y_ in y_]
plt.scatter(x, y, c="c")

# 2
x_bar = np.mean(x)
y_bar = np.mean(y)

xy_sum = 0
x_sum = 0

n = range(len(x))
for i in n:
	xy_sum += x[i] * y[i]
	x_sum += x[i] ** 2

w = (xy_sum - n * x_bar * y_bar) / (x_sum - n * x_bar ** 2)
b = y_bar - w * x_bar

print("w=",w, "b=", b)
print("y=" + str(np.round_(w,2)) + "x+" + str(np.round_(b,2)))

plt.plot(x, w * x + b, "r-")
plt.show()
