import random
import math
import histogram
import numpy as np
import matplotlib.pyplot as plt
import polygon

# Пользовательский ввод данных
def input_use(text):
    # Ввод интервала (a, b)
    while True:
        try:
            value1, value2 = map(int, input(text).split())
            break
        except:
            print("Некорректный ввод.")
    return value1, value2

# Пункт 1: метод обратных функций
# нахождение x[i] от случайной величины r[i]
def find_xi(a, b, ri):
    return ri * (b - a) + a

# Пункт 2: гауссовский закон с параметрами N(m,б^2) на основе ЦПТ
# формула замены
def fun_replacement(v, m, g):
    return (v - m) / g

# Пункт 3: Метод Неймана
# нахождение максимума расределения Рэлея
def find_max(g):
    return (1 / g) * math.exp(-1 / 2)

# Пункт 3: Метод Неймана
# нахождение g(x)
def q(g, X):
    return X * math.exp(-X ** 2 / 2 * g ** 2)


# Массив для случайных величин
r = []
# Массивы для каждого пункта
x = [[], [], []]
# Объем выборки
N = int(input(f"Введите N (6<=N<=12): "))
# Интервал (a,b)
a = 0
b = 0
# Запрашиваем ввод пользователя
while a >= b:
    a, b = input_use(f"Введите интервал (a, b), при чем a<b. Пример: 6 12\n")
    if a >= b:
        print("Некорректный ввод.")
# m, g = input_use(f"Введите m и б. Пример: 6 12\n")

# Находим максимум распределения Рэлея
# M = find_max(g)

# for j in range(1000):
#     for i in range(N):
#         # пункт 1: метод обратных функций
#         # находим xi от сулчайной величины ri
#         r.append(random.random())
#         if len(x[0]) < 1000:
#             x[0].append(find_xi(a, b, r[i]))
#
#
# for i in range(len(x)):
#     x[i].sort()

# Вводим число интервалов группировки
K = int(input(f"Введите количесво интервалов 10<k<21: "))
# нужно для одинакоых примеров
np.random.seed(10)
# генерируем 1000 случайных чисел
# for j in range(N):
r = np.random.rand(1000)
for i in range(len(r)):
    x[0].append(find_xi(a, b, r[i]))

# сортируем выборку x
for i in range(len(x)):
    x[i].sort()
index = 0
histogram.histogram(x[0], a, b, K, index)
# histogram.histogram(x[1], (1 - 0.02) * min(x[1]), (1 + 0.02) * max(x[1]), K)
plt.show()

# for j in range(1000):
#     v = 0
#     for i in range(N):
#         r.append(random.random())
#         v += r[i]
#         if len(x[0]) < 1000 and i == 0:
#             # 1 пункт: find_xi - метод обратных функций
#             x[0].append(find_xi(a, b, r[0]))
#         if i > 0 and len(x[2]) < 1000:
#             # 3 пункт: метод Неймана
#             X = a + (b - a) * r[i - 1]
#             if M * r[i] < q(g, X):
#                 x[2].append(X)
#     # 2 пункт: ЦПТ
#     xi = (v - m) / g
#     x[1].append(xi)
#     # Освобождаем ресурсы
#     r.clear()

# # Номер графа
# index = 0
# # Постоение гистограмм
# for i in range(len(x)):
#     # Если в массиве есть величины
#     if len(x[i]) > 0:
#         index += 1
#         # Рисуем гистограмму
#         g, K = histogram.create_histogram(x[i], index)
#         index += 1
#         # plt.subplot (2, 3, index)
#         # plt.hist(g, bins=K)
#         # plt.show()
#         # Рисуем ступенчатую диаграмму
#         polygon.new_tree(g, K, index)
#         # plt.show()
#         # print(len(g), len(F))
#         # index += 1
#         # plt.subplot(2, 3, index)
#         # plt.step(F, K)
#     print(len(x[i]))
# plt.show()
