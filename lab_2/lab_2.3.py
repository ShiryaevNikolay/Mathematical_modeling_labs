import functions as fun
import numpy as np
# import lab_2.piecewice_parabolic_interpolation as interpolation

points = fun.openFile(r"C:\Users\deend\Desktop\Мат. моделирование\data_points.xlsx")

inputData = fun.inputUser(points)
graph = fun.paintGraph(inputData, points)

# Функция нахождения координат для кусочно-параболической интерполяции
def findNewCoordinates(x, y):
    # Оригинальные значения координат
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    # Находим новые координаты
    for i in range(1, len(x)-1):
        xnew = np.linspace(np.min(x[i-1]), np.max(x[i+1]), 100)
        ynew = [fun.piecewice_parabolic_interpolation(x, y, i, xl) for xl in xnew]
        graph.plot(xnew, ynew)
    return graph


# Если пользователь ввел одно число
if len(inputData) == 1:
    # Если ввели 0, то рисуем все графики
    if int(inputData[0]) == 0:
        # Пробегаемся по каждому набору координат отдельного графика
        for point in range(len(points)):
            graph = findNewCoordinates(point[0], point[1])
        graph.show()
    else:   # Иначе рисуем один график
        graph = findNewCoordinates(points[int(inputData[0]) - 1][0], points[int(inputData[0]) - 1][1])
        graph.show()
elif len(inputData) == 2:   # Если пользователь ввел диапозон
    # Записываем границы диапозона в переменные
    minValue = int(inputData[0])-1
    maxValue = int(inputData[1])
    print(minValue, " ", maxValue)
    # Пробегаемся по каждому набору координат отдельного графика
    for point in range(minValue, maxValue):
        graph = findNewCoordinates(points[point][0], points[point][1])
    graph.show()