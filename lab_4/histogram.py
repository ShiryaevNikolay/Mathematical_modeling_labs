import matplotlib.pyplot as plt
import polygon
import numpy as np


def histogram(point, x, a, b, m, sigma):
    N = len(x)
    # Определяется длина группировки
    d = b - a
    k = int(1 + np.log2(N))
    deltaX = d / k
    # частоты бi
    g = []
    # wx
    # wx = [a]
    gx = []
    for i in range(k):
        sum = 0
        # границы интервала
        deltaiMin = a + i*deltaX
        deltaiMax = a + (i + 1)*deltaX
        # wx.append(deltaiMax)
        gx.append((deltaiMax + deltaiMin) / 2)
        for j in range(N):
            if deltaiMin < x[j] <= deltaiMax:
                # Колличество ki элементов выборки, попавших в
                # интервал группировки deltai
                sum += 1
        # Определяется частота бi
        g.append(sum / (N * deltaX))
    # Строим гистограмму
    plt.bar(gx, g, width=deltaX, alpha=0.5)
    if point == 0:
        plt.title("Равномерное распределение")
        # строим плотность равномерного распределения
        wx_even(a, b, x)
    elif point == 1:
        plt.title("Нормальное распределение")
        # строим плотность гауссовского распределения
        wx_gauss(x, m, sigma)
    elif point == 2:
        plt.title("Распределение Рэлея")
        print(np.sort(g))
        wx_rayleigh(x, sigma)
    plt.show()
    # вызываем функцию построения ступенчатой диаграммы
    polygon.step_fun(point, a, b, deltaX, N, x, k, m, sigma)


# нахождение плотности равномерного распределения
def wx_even(a, b, wx):
    wy = []
    for i in range(len(wx)):
        wy.append((1 / (b - a)))
    plt.plot(wx, wy, color='r')


# нахождение плотности гауссовского распределения
def wx_gauss(wx, m, sigma):
    wy = []
    for i in range(len(wx)):
        wy.append((1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-1 * (wx[i] - m)**2 / (2 * (sigma ** 2))))
    plt.plot(wx, wy, color='r')


# нахождение плотности элеевского распределения
def wx_rayleigh(wx, sigma):
    wy = []
    for i in range(len(wx)):
        wy.append((wx[i] / (sigma ** 2)) * np.exp(-1 * ((wx[i] ** 2) / (2 * (sigma ** 2)))))
    plt.plot(wx, wy, color='r')
