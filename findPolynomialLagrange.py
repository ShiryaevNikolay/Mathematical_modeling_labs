import numpy as np

def polynomialLagrange(x, y, xnew):
    ynew = []
    # Провегаем по всем новым значениям xnew
    for xl in xnew:
        # Полином Лагранжа
        L = 0
        # Пробегаем по всем X[i]
        for i in range(len(x)):
            # Промежуточные значения дроби полинома
            p1 = 1
            p2 = 1
            # Пробегаем по всем X[j]
            for j in range(len(x)):
                # i != j по условию, так как p2 будет равен 0
                if i == j:
                    continue
                # Вычисляем числитель и знаменатель
                p1 = p1 * (xl - x[j])
                p2 = p2 * (x[i] - x[j])
            # Находим поленом L[i]
            L = L + y[i] * p1 / p2
        # Добавляем L[i] в новый массив значений y
        ynew.append(L)
    return ynew

def getPolynomialLagrange(x, y, graph):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    xnew = np.linspace(np.min(x), np.max(x), 100)
    ynew = polynomialLagrange(x, y, xnew)
    graph.plot(x, y, 'o', xnew, ynew)
    graph.grid(True)
    return graph