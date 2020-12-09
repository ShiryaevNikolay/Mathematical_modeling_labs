import matplotlib.pyplot as plt
import seaborn as sns
import polygon

def histogram(x, a, b, K, index):
    N = len(x)
    # Определяется длина и границы группировки
    d = b - a
    deltaX = d / K
    sum = []
    # частоты бi
    g = []
    for i in range(K):
        sum.append(0)
        # границы интервала
        deltaiMin = a + i*deltaX
        deltaiMax = a + (i + 1)*deltaX
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
    plt.subplot(1, 2, index)
    sns.distplot(x, bins=K)
    # вызываем функцию построения ступенчатой диаграммы
    polygon.tree(a, deltaX, N, x, K, index)
