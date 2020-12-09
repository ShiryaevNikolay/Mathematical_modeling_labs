# Функция нахождения математического ожидания
def expected(x):
    N = len(x)
    m = 0
    for i in range(N):
        m += x[i]
    m = m / N
    print(f"Математическое ожидание m: ", m)
    variance(x, m)


# Функция нахождения дисперсии
def variance(x, m):
    N = len(x)
    d = 0
    for i in range(N):
        d += (x[i] - m)**2
    d = d / N
    print(f"исперсия d: ", d)
