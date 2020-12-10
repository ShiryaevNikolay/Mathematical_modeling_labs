import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats as st
import polygon
import numpy as np

def histogram(point, x, a, b, K, index, m, sigma):
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
    plt.hist(x, bins=K)
    if point == 0:
        plt.title("Равномерное распределение")
        # строим плотность равномерного распределения
        wx_even(a, b, sum, wx)
    elif point == 1:
        plt.title("Нормальное распределение")
        # строим плотность гауссовского распределения
        wx_gauss(wx, m, sigma, np.max(sum))
    # elif point == 2:
    #     plt.title("Распределение Рэлея")
    #     wx_rayleigh(wx, sigma)
    plt.show()
    # вызываем функцию построения ступенчатой диаграммы
    polygon.step_fun(point, a, b, deltaX, N, x, K, index, m, sigma)


# нахождение плотности непрерывного распределения
def wx_even(a, b, sum, wx):
    h = np.sum(sum) / len(sum)
    wy = []
    for i in range(len(wx)):
        wy.append((1 / (b - a)) + h)
    plt.plot(wx, wy, linewidth=3, color='r')


# нахождение плотности гауссовского распределения
def wx_gauss(wx, m, sigma, Ymax):
    # находим границы графика
    a = np.min(wx)
    b = np.max(wx)
    # добавляем точки, чтотбы график был гладкий
    wx = np.linspace(a, b, 500)
    wy = []
    for i in range(len(wx)):
        wy.append((1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-1 * (wx[i] - m)**2 / (2 * sigma ** 2)))
    for i in range(len(wy)):
        wy[i] = wy[i] * 300
    # находим Ymin чтобы опустить график на ось Х
    ymin = np.min(wy)
    # опускаем каждое значение У на величину Ymin
    for i in range(len(wy)):
        wy[i] = wy[i] - ymin
    plt.plot(wx, wy, linewidth=3, color='r')


# нахождение плотности элеевского распределения
def wx_rayleigh(wx, sigma):
    # находим границы графика
    a = np.min(wx)
    b = np.max(wx)
    # добавляем точки, чтотбы график был гладкий
    wx = np.linspace(a, b, 1000)
    wy = []
    for i in range(len(wx)):
        wy.append((wx[i] / sigma ** 2) * np.exp(-(wx[i] ** 2) / (2 * sigma ** 2)))
    # делаем пропорции координат
    for i in range(len(wy)):
        wy[i] = wy[i] * 100
    # находим Ymin чтобы опустить график на ось Х
    ymin = np.min(wy)
    # опускаем каждое значение У на величину Ymin
    for i in range(len(wy)):
        wy[i] = wy[i] - ymin
    plt.plot(wx, wy, linewidth=3, color='r')
