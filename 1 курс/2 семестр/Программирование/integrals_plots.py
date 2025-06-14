import numpy as np
import matplotlib.pyplot as plt

# Функция
def f(x):
    return 32 + 28 * x - 9 * x**2

# Интервал и число разбиений
a, b = 2, 4
n = 6
x = np.linspace(a, b, 400)
hx = (b - a) / n
x_nodes = np.linspace(a, b, n + 1)

# --- Левый метод ---
fig, ax = plt.subplots()
ax.plot(x, f(x), 'b', label='f(x)')
for i in range(n):
    xi = x_nodes[i]
    ax.bar(xi, f(xi), width=hx, align='edge', edgecolor='black', alpha=0.4)
# ax.set_title('Метод левых прямоугольников')
ax.legend()
plt.grid(True)
plt.savefig("left_rectangles.png")

# --- Правый метод ---
fig, ax = plt.subplots()
ax.plot(x, f(x), 'b', label='f(x)')
for i in range(n):
    xi = x_nodes[i + 1]
    ax.bar(xi - hx, f(xi), width=hx, align='edge', edgecolor='black', alpha=0.4)
# ax.set_title('Метод правых прямоугольников')
ax.legend()
plt.grid(True)
plt.savefig("right_rectangles.png")

# --- Средний метод ---
fig, ax = plt.subplots()
ax.plot(x, f(x), 'b', label='f(x)')
for i in range(n):
    xi = x_nodes[i]
    mid = xi + hx / 2
    ax.bar(mid - hx/2, f(mid), width=hx, align='edge', edgecolor='black', alpha=0.4)
# ax.set_title('Метод средних прямоугольников')
ax.legend()
plt.grid(True)
plt.savefig("mid_rectangles.png")

# --- Метод трапеций ---
fig, ax = plt.subplots()
ax.plot(x, f(x), 'b', label='f(x)')
for i in range(n):
    x0 = x_nodes[i]
    x1 = x_nodes[i + 1]
    y0 = f(x0)
    y1 = f(x1)
    ax.fill([x0, x0, x1, x1], [0, y0, y1, 0], 'orange', edgecolor='black', alpha=0.4)
# ax.set_title('Метод трапеций')
ax.legend()
plt.grid(True)
plt.savefig("trapezoid.png")

plt.show()

