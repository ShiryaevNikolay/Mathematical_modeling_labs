import matplotlib.pyplot as plt

def tree(a, deltaX, N, x, K, index):
    k = []
    F = [0]
    fx = [a]
    for q in range(K):
        k.append(0)
        b = a + (q + 1) * deltaX
        fx.append(b)
        for i in range(len(x)):
            if a <= x[i] < b:
                k[q] += 1
        F.append(k[q] / N)
    index += 1
    plt.subplot(1, 2, index)
    plt.step(fx, F)
    plt.show()

def new_tree(g, K, index):
    g.sort()
    F = []
    sum = 0
    for gi in g:
        sum += gi
        F.append(sum)
    print(F)
    index += 1
    plt.subplot(1, 2, index)
    plt.step(g, F)