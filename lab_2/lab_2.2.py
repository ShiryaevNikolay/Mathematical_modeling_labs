import functions as fun
import numpy as np
import lab_2.piecewice_linear_interpolation as polinomial

points = fun.openFile(r"C:\Users\deend\Desktop\Мат. моделирование\data_points.xlsx")

inputData = fun.inputUser(points)
graph = fun.paintGraph(inputData, points)

def findPolinomial(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    xnew = np.linspace(np.min(x), np.max(x), 100)
    ynew = [polinomial.piecewice_linear_interpolation(x, y, xl) for xl in xnew]
    graph.plot(x, y, 'o', xnew, ynew)
    return graph

# Если пользователь ввел одно число
if len(inputData) == 1:
    # Если ввели 0, то рисуем все графики
    if int(inputData[0]) == 0:
        # Пробегаемся по каждому набору координат отдельного графика
        for point in range(len(points)):
            graph = findPolinomial(point[0], point[1])
        graph.show()
    else:   # Иначе рисуем один график
        graph = findPolinomial(points[int(inputData[0])-1][0], points[int(inputData[0])-1][1])
        graph.show()
elif len(inputData) == 2:   # Если пользователь ввел диапозон
    # Записываем границы диапозона в переменные
    minValue = int(inputData[0])-1
    maxValue = int(inputData[1])
    print(minValue, " ", maxValue)
    # Пробегаемся по каждому набору координат отдельного графика
    for point in range(minValue, maxValue):
        graph = findPolinomial(points[point][0], points[point][1])
    graph.show()
