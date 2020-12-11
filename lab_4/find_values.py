# Функция нахождения математического ожидания
def expected(x):
    N = len(x)
    m = 0
    for i in range(N):
        m += x[i]
    m = m / N
    print(f"Выборочное m: ", m)
    return variance(x, m)


# Функция нахождения дисперсии
def variance(x, m):
    N = len(x)
    sigma = 0
    for i in range(N):
        sigma += (x[i] - m)**2
    sigma = sigma / N
    print(f"Выборочная дисперсия sigma2: ", sigma)
    return m, sigma
