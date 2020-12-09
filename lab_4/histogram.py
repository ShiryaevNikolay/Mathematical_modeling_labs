import matplotlib.pyplot as plt
import polygon

def histogram(x, a, b, K):
    # N = len(x)
    # # Определяется длина и границы группировки
    # # d = 1.02 * (max(x) - min(x))
    # d = b - a
    # deltaX = d / K
    # k = []
    # g = []
    # for i in range(K):
    #     k.append(0)
    #     deltaiMin = a + i*deltaX
    #     deltaiMax = a + (i + 1)*deltaX
    #     print(deltaiMin, deltaiMax)
    #     for j in range(N):
    #         if deltaiMin <= x[j] < deltaiMax:
    #             # Колличество ki элементов выборки, попавших в
    #             # интервал группировки deltai
    #             k[i] += 1
    #             # print(x[j])
    #     # Определяется частота бi
    #     print(k[i])
    #     g.append(k[i] / N)
    # plt.hist(g, bins=K)
    plt.hist(x, bins=K)
    print("X = ", x)
    # print("g = ", g)
