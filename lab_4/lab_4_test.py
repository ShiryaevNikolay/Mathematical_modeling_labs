import histogram
import numpy as np
import find_values as val


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
# def fun_replacement(v, m, g):
#     return (v - m) / g
def fun_replacement(v, n):
    return np.sqrt(12/n) * v


# Пункт 3: Метод Неймана
# нахождение максимума расределения Рэлея
def find_max(g):
    return (g / (g**2)) * np.exp(-1 * (g**2) / 2 * (g**2))


# Пункт 3: Метод Неймана
# нахождение g(x)
def q(g, X):
    return (X) * np.exp(-1 * (X ** 2) / 2 * (g ** 2))


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
m = float(input("Введите m: "))
g = float(input("Введите б: "))

# Находим максимум распределения Рэлея
M = find_max(g)

# Вводим число интервалов группировки
K = int(input(f"Введите количесво интервалов 10<k<21: "))
# находим выборки для каждого пункта
for j in range(1000):
    v = 0
    for i in range(N):
        ri = np.random.random()
        r.append(ri)
        v += ri
        if len(x[0]) < 1000:
            # пункт 1: непрерывные величины
            x[0].append(find_xi(a, b, ri))
        if len(x[2]) < 1000:
            # пункт 3: метод Неймана
            # X = g * (np.sqrt(-2*np.log(r[i - 1])))
            X = a + (b - a) * r[i - 1]
            if M * r[i] < q(g, X):
                x[2].append(X)
    # пункт 2: ЦПТ
    # x[1].append(fun_replacement(v, m, g))
    x[1].append(fun_replacement(v, N))
    # Освобождаем ресурсы
    r.clear()

# print(len(x[2]))
# print(x[2])

# сортируем выборку x
for i in range(len(x)):
    x[i].sort()
index = 0
# строим графики для каждой выборки
histogram.histogram(0, x[0], a, b, K, index)
# histogram.histogram(x[1], (1 - 0.02)*np.min(x[1]), (1 + 0.02)*np.max(x[1]), K, index)
# if len(x[2]) > 0:
#     histogram.histogram(x[2], (1 - 0.02) * min(x[2]), (1 + 0.02) * max(x[2]), K, index)

# for i in range(len(x)):
#     val.expected(x[i])
