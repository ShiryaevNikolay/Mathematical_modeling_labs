import matplotlib.pyplot as plt
import scipy.stats as st
import seaborn as sns
import polygon
import find_values as val
import numpy as np

def histogram(point, x, a, b, K, index):
    N = len(x)
    # Определяется длина и границы группировки
    d = b - a
    deltaX = d / K
    sum = []
    # частоты бi
    g = []
    # wx
    wx = [a]
    for i in range(K):
        sum.append(0)
        # границы интервала
        deltaiMin = a + i*deltaX
        deltaiMax = a + (i + 1)*deltaX
        wx.append(deltaiMax)
        for j in range(N):
            if deltaiMin <= x[j] < deltaiMax:
                # Колличество ki элементов выборки, попавших в
                # интервал группировки deltai
                sum[i] += 1
                # print(x[j])
        # Определяется частота бi
        g.append(sum[i] / N)
    # Строим гистограмму
    index += 1  # индекс для размещения двух графиков в олном окне
    # plt.subplot(1, 2, index)
    # sns.distplot(x, bins=K, kde=False)
    plt.hist(x, bins=K)
    if point == 0:
        # строим плотность равномерного распределения
        even(a, b, sum, wx)
    plt.show()
    # вызываем функцию построения ступенчатой диаграммы
    polygon.step_fun(point, a, b, deltaX, N, x, K, index)


# нахождение функции непрерывного распределения
def even(a, b, sum, wx):
    h = np.sum(sum) / len(sum)
    wy = []
    for i in range(len(wx)):
        wy.append((1 / (b - a)) + h)
    plt.plot(wx, wy, linewidth=3, color='r')
