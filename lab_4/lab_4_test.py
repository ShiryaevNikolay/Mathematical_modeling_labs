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
def fun_gauss(v, m, sigma):
    return (v - m) / sigma
# def fun_gauss(v, n):
#     return np.sqrt(12/n) * v


# Пункт 3: Метод Неймана
# нахождение максимума расределения Рэлея
def find_max(sigma):
    return (1 / sigma) * np.exp(-1 / 2)


# Пункт 3: Метод Неймана
# нахождение sigma(x)
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
# m, sigma = input_use(f"Введите m и б. Пример: 6 12\n")
m = float(input("Введите m: "))
sigma = float(input("Введите sigma: "))

# Находим максимум распределения Рэлея
M = find_max(sigma)

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
            X = sigma * (np.sqrt(-2 * np.log(r[i - 1])))
            # X = a + (b - a) * r[i - 1]
            if M * r[i] < q(sigma, X):
                x[2].append(X)
    # пункт 2: ЦПТ
    # x[1].append(fun_gauss(v, N))
    x[1].append(fun_gauss(v, m, sigma))
    # Освобождаем ресурсы
    r.clear()

# сортируем выборку x
for i in range(len(x)):
    x[i].sort()
index = 0
# строим графики для каждой выборки
histogram.histogram(0, x[0], a, b, K, index, m, sigma)
histogram.histogram(1, x[1], (1 - 0.02) * np.min(x[1]), (1 + 0.02) * np.max(x[1]), K, index, m, sigma)
if len(x[2]) > 0:
    histogram.histogram(2, x[2], (1 - 0.02) * min(x[2]), (1 + 0.02) * max(x[2]), K, index, m, sigma)

print("---------------------------------------------")
print("Непрерывное распределение")
print("m: ", (b + a) / 2)
print("s2: ", (b - a)**2 / 12)
val.expected(x[0])
print("---------------------------------------------")
print("Нормальное распределение (Гаусса)")
print("m: ", m)
print("s2: ", sigma)
val.expected(x[1])
print("---------------------------------------------")
print("Распределение Рэлея")
print("m: ", np.sqrt((np.pi * sigma**2) / 2))
print("s2: ", sigma)
val.expected(x[2])
