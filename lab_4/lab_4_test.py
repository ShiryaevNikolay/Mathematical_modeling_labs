import random
import math


def input_use(text):
    # Ввод интервала (a, b)
    while True:
        try:
            value1, value2 = map(int, input(text).split())
            break
        except:
            print("Некорректный ввод.")
    return value1, value2


def find_xi(a, b, ri):
    return ri * (b - a) + a


def find_max(g):
    return (1 / g) * math.exp(-1 / 2)


def q(g, X):
    return X * math.exp(-X ** 2 / 2 * g ** 2)


# Массив для случайных величин
r = []
# Массивы для каждого пункта
x1 = []
x2 = []
x3 = []
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
        if i > 0 and len(x3) < 1000:
            # 3 пункт
            X = a + (b - a) * r[i - 1]
            if M * r[i] < q(g, X):
                x3.append(X)
    # 1 пункт
    x1.append(find_xi(a, b, r[0]))
    # 2 пункт
    xi = (v - m) / g
    x2.append(xi)
    # Освобождаем ресурсы
    r.clear()
print(len(x1))
print(len(x2))
print(len(x3))
