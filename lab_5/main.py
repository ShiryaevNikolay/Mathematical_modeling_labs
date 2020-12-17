from lab_5.simple_iteration_method import *
from lab_5.newton_method import *
import matplotlib.pyplot as plt


def create_plot(x, y1, y2, title):
    plt.title(title)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.grid(True)
    plt.show()

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

# Строим график функций для наглядности
x = np.linspace(intervalA, intervalB, 1000)
y1 = fun_with_param(a, b, x)
y2 = fun(x)


print("\n-----------------------------------------------------------------")
print("Метод простых итераций")

# Ищем приближение для функции с параметрами
iteration_method_with_param(x0, eps, a, b)
# Ищем приближение для функции без параметрами
iteration_method_without_param(x0, eps)

# Показываем графики для метода простых итераций
create_plot(x, y1, y2, "Метод простых итераций")

print("-----------------------------------------------------------------")
print("Метод Ньютона")

# Ищем приближение для функции с параметрами
newton_method_with_param(x0, n, a, b)
# Ищем приближение для функции без параметрами
newton_method_without_param(x0, n)

# Показываем графики для метода Ньютона
create_plot(x, y1, y2, "Метод Ньютона")

print("-----------------------------------------------------------------")


