import matplotlib.pyplot as plt
import numpy as np
import polygon

def histogram(x, a, b, K, index):
    N = len(x)
    # Определяется длина и границы группировки
    d = b - a
    deltaX = d / K
    k = []
    # координаты по оси Х для построения линии
    kx = []
    # частоты бi
    g = []
    for i in range(K):
        k.append(0)
        # границы интервала
        deltaiMin = a + i*deltaX
        deltaiMax = a + (i + 1)*deltaX
        # получаем координату x для интервала deltai
        kx.append((deltaiMax + deltaiMin) / 2)
        for j in range(N):
            if deltaiMin <= x[j] < deltaiMax:
                # Колличество ki элементов выборки, попавших в
                # интервал группировки deltai
                k[i] += 1
                # print(x[j])
        # Определяется частота бi
        g.append(k[i] / N)
    # Строим гистограмму
    index += 1
    plt.subplot(1, 2, index)
    plt.hist(x, bins=K)
    plt.title("Непрерывные величины")
    # строим линию распределения
    fx = np.linspace(np.min(kx), np.max(kx))
    fp = np.polyfit(kx, k, 7)
    fy = np.poly1d(fp)
    plt.plot(fx, fy(fx), linewidth=3)
    # polygon.new_tree(g, K, index)
    polygon.tree(a, deltaX, N, x, K, index)
