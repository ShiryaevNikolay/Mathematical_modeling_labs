from lab_5.simple_iteration_method import *
from lab_5.newton_method import *
from lab_5.dichotomy_method import *
import matplotlib.pyplot as plt


def create_plot(x, y1, y2, title):
    plt.title(title)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.grid(True)
    plt.show()


# Вводим начальные значения
a = float(input("Параметр a: "))
b = float(input("Параметр b: "))

x0 = int(input("Начальное приближение x0: "))
eps = float(input("Точность eps: "))
n = int(input("Число итераций n: "))

intervalA = float(input("Граница интервала A: "))
intervalB = float(input("Граница интервала B: "))
# intervalA = -1
# intervalB = 1

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
print("Метод дихотомии")

# Ищем приближение для функции с параметрами
dichotomy_method_with_param(eps, a, b, intervalA, intervalB)
# Ищем приближение для функции без параметрами
dichotomy_method_without_param(eps, intervalA, intervalB)

# Показываем графики для метода дихотомии
create_plot(x, y1, y2, "Метод дихотомии")
