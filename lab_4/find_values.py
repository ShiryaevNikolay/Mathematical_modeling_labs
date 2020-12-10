# Функция нахождения математического ожидания
def expected(x):
    N = len(x)
    m = 0
    for i in range(N):
        m += x[i]
    m = m / N
    print(f"Математическое ожидание m: ", m)
    return variance(x, m)


# Функция нахождения дисперсии
def variance(x, m):
    N = len(x)
    s2 = 0
    for i in range(N):
        s2 += (x[i] - m)**2
    s2 = s2 / N
    print(f"Дисперсия s2: ", s2)
    return m, s2
