import matplotlib.pyplot as plt
import seaborn as sns

def tree(a, deltaX, N, x, K, index):
    # массив для хранения количества xi, попавших в интервал
    sum = []
    # массив выборочных вероятностей
    F = [0]
    # массив для хранения координат по оси Х
    fx = [a]
    for q in range(K):
        sum.append(0)
        # правая граница интервала
        b = a + (q + 1) * deltaX
        fx.append(b)
        for i in range(len(x)):
            # если xi попадает в интервал, то добавляем в массив сумм
            if a <= x[i] < b:
                sum[q] += 1
        F.append(sum[q] / N)
    # индекс для постоения двух графиков на одном окне
    index += 1
    # строим ступенчатую диаграмму и показываем графики
    plt.subplot(1, 2, index)
    sns.lineplot(fx, F, drawstyle='steps-pre')
    plt.show()
