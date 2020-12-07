import functions as fun
import numpy as np
from scipy import interpolate

points = fun.openFile(r"..\data_points.xlsx")

inputData = fun.inputUser(points)
graph = fun.paintGraph(inputData, points)

# Функция нахождения координат для сплайн интерполяции (стандартной библиотеки python)
def findNewCoordinates(x, y):
    # Оригинальные значения координат
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    # Находим новые координаты
    xnew = np.linspace(np.min(x), np.max(x), 100)
    tck = interpolate.splrep(x, y, s=0)
    ynew = interpolate.splev(xnew, tck, der=0)
    graph.plot(x, y, 'o', xnew, ynew)
    return graph

# Если пользователь ввел одно число
if len(inputData) == 1:
    # Если ввели 0, то рисуем все графики
    if int(inputData[0]) == 0:
        # Пробегаемся по каждому набору координат отдельного графика
        for point in range(len(points)):
            graph = findNewCoordinates(point[0], point[1])
    else:   # Иначе рисуем один график
        graph = findNewCoordinates(points[int(inputData[0]) - 1][0], points[int(inputData[0]) - 1][1])
elif len(inputData) == 2:   # Если пользователь ввел диапозон
    # Записываем границы диапозона в переменные
    minValue = int(inputData[0])-1
    maxValue = int(inputData[1])
    print(minValue, " ", maxValue)
    # Пробегаемся по каждому набору координат отдельного графика
    for point in range(minValue, maxValue):
        graph = findNewCoordinates(points[point][0], points[point][1])

graph.show()