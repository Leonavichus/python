# Вариант - 10
# y = esin(ax2+bx+c)+dcos(fx+g)

import numpy as np
import matplotlib.pyplot as plt

def z(x, a, b, c, d, f, g):
    a = a
    b = b
    c = c
    d = d
    f = f
    g = g

    return np.e * np.sin(a * x ** 2 + b * x + c) + d * np.cos(f * x + g)

num1 = float(input('a = '))
num2 = float(input('b = '))
num3 = float(input('c = '))
num4 = float(input('d = '))
num5 = float(input('f = '))
num6 = float(input('g = '))

xx = np.arange(-10, 11, 1)
yy = z(xx, num1, num2, num3, num4, num5, num6)

fig, ax = plt.subplots()

ax.plot(xx, yy)
ax.grid(linestyle=":")

plt.show()
