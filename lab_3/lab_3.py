import functions as fun
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

points = fun.openFile(r"C:\Users\deend\Desktop\Мат. моделирование\data_points.xlsx")
k = len(points[0][0])


# Функция запроса пользовательского ввода
def inputUser(points):
    # Выводи количество точек в консоль
    while True:
        # Запрашиваем ввод
        n = input(f"Количесво точек: {points}\n"
                  f"Введите n такое, что 1<n<20: ")
        # Нужно для проверки ввода
        сorrectInput = False
        try:
            if 1 <= int(n) <= points:
                сorrectInput = True
                return int(n)
        except:
            print("Некорректный ввод")

def paintGraph(x, y):
    plt.grid(True)
    plt.scatter(x, y)
    return plt

# Запрашиваем ввод пользователя
n = inputUser(len(points[0][0]))

x = points[0][0]
y = points[0][1]

graph = paintGraph(x, y)

# Аргументы для постоения графиков
fx = np.linspace(np.min(x), np.max(x))
# Получвем параметры для полинома n-ой степени
fp = np.polyfit(x, y, n)
# функция-полином
fy = np.poly1d(fp)
graph.plot(fx, fy(fx))

graph.show()
