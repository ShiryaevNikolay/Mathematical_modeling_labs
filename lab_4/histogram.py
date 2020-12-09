import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy import interpolate
import polygon

def histogram(x, a, b, K):
    N = len(x)
    # Определяется длина и границы группировки
    # d = 1.02 * (max(x) - min(x))
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
    plt.hist(x, bins=K)
    # строим линию распределения
    fx = np.linspace(np.min(kx), np.max(kx))
    fp = np.polyfit(kx, k, 7)
    fy = np.poly1d(fp)
    plt.plot(fx, fy(fx), linewidth=3)
