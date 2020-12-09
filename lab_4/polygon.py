import matplotlib.pyplot as plt

def tree(a, dx, N, x):
    k = []
    F = []
    dq = []
    for q in range(N):
        dq.append(q)
        k.append(0)
        dmax = a + q * dx
        for i in range(N):
            if a <= x[i] <= dmax:
                k[q] += 1
        F.append(k[q] / N)
    return plt.step(F, dq)

def new_tree(g, K, index):
    g.sort()
    F = []
    sum = 0
    for gi in g:
        sum += gi
        F.append(sum)
    print(F)
    plt.subplot(2, 3, index)
    plt.step(F, g)