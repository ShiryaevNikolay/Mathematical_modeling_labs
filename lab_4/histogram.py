def create_histogram(x):
    N = len(x)
    K = int(input(f"Введите количесво интервалов 10<k<21: "))

    a = (1 - 0.02) * x[0]
    b = (1 + 0.02) * x[N - 1]
    d = 1.02 * (x[N - 1] - x[0])
    dx = d / K

    k = []
    g = []
    for i in range(K):
        k.append(0)
        dmin = a + (i - 1) * dx
        dmax = a + i * dx
        for j in range(N):
            if dmin <= x[j] <= dmax:
                k[i] += 1
        g.append(k[i] / N)
    return g, K
