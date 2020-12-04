import random


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


r = []
for i in range(6000):
    # Получаем случайные знамения на интервале (0,1) и заполняем массив r
    r.append(random.random())

a = 0
b = 0
# Запрашиваем ввод пользователя
while a >= b:
    a, b = input_use(f"Введите интервал (a, b), при чем a<b. Пример: 6 12\n")
    if a >= b:
        print("Некорректный ввод.")
m, d = input_use(f"Введите мат. ожидание и ср. кв. отклонение. Пример: 6 12\n")

'''Задание 1.1: Метод обратных функций'''
# print(a, b)
x1 = []
for i in range(1000):
    # Заполняем массив x1
    x1.append(find_xi(a, b, r[i]))
print(len(x1))

'''Задание 1.2: Распределение по гауссовскому закону 
    с параметрами N(m, б^2) на основе ЦПТ'''
x2 = []
for i in range(0, len(r)-5, 6):
    v = 0
    for j in range(i, i+6):
        v += r[j]
    xi = (v - m) / d
    x2.append(xi)
print(len(x2))

'''Задание 1.3: Метод Неймона'''
x3 = []

