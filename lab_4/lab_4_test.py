import random
import math
import histogram
import matplotlib.pyplot as plt

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
# x1 = []
# x2 = []
# x3 = []
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
m, g = input_use(f"Введите m и б. Пример: 6 12\n")

# Находим максимум распределения Рэлея
M = find_max(g)

for j in range(1000):
    v = 0
    for i in range(N):
        r.append(random.random())
        v += r[i]
        if len(x[0]) < 1000:
            # 1 пункт
            x[0].append(find_xi(a, b, r[0]))
        if i > 0 and len(x[2]) < 1000:
            # 3 пункт
            X = a + (b - a) * r[i - 1]
            if M * r[i] < q(g, X):
                x[2].append(X)
    # 2 пункт
    xi = (v - m) / g
    x[1].append(xi)
    # Освобождаем ресурсы
    r.clear()

# Постоение гистограмм
for xi in x:
    if len(xi) > 0:
        g, K = histogram.create_histogram(xi)
        plt.hist(g, bins=K)
    print(len(xi))
plt.grid(True)
plt.show()
