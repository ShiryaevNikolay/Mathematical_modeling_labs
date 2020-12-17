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
y1 = fun_with_param(a, b, x)
y2 = fun(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid(True)

# Ищем приближение для функции с параметрами
iteration_method_with_param(x0, eps, a, b)
# Ищем приближение для функции без параметрами
iteration_method_without_param(x0, eps)

# Показываем графики для метода простых итераций
plt.show()


