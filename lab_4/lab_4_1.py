import random


def find_xi(a, b, ri):
    return ri * (b - a) + a


# Ввод интервала (a, b)
while True:
    try:
        a, b = map(int, input(f"Введите интервал (a, b), при чем a<b. Пример: 6 12\n").split())
        if a > b:
            print("Некорректный ввод.")
            continue
        break
    except:
        print("Некорректный ввод.")
print(a, b)
r = []
x = []
for i in range(1000):
    # Получаем знамения ri на интервале (0,1)
    ri = random.random()
    # Заполняем массив r
    r.append(ri)
    # Заполняем массив x
    x.append(find_xi(a, b, ri))
# Сортируем массивы по возрастанию
r.sort()
x.sort()
print(x)
