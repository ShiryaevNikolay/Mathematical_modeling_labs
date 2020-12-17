from lab_5.equations import *
from lab_5.simple_iteration_method import *
import matplotlib.pyplot as plt


# Вводим начальные значения
x0 = int(input("Начальное приближение x0: "))
eps = float(input("Точность eps: "))
n = int(input("Число итераций n: "))
# intervalA = float(input("Граница интервала a: "))
# intervalB = float(input("Граница интервала b: "))
intervalA = -1
intervalB = 1

a = float(input("Параметр a: "))
b = float(input("Параметр b: "))

# Строим график функции с параметрами для наглядности
x = np.linspace(intervalA, intervalB, 1000)
y = []
for xi in x:
    y.append(fun_with_param(a, b, xi))
plt.plot(x, y)
plt.grid(True)

iteration_method(x0, eps, a, b)
plt.show()
