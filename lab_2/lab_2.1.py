import functions as fun
import findPolynomialLagrange as lagrange

# Путь к файлу
points = fun.openFile(r"..\data_points.xlsx")

# Ввод пользовательких данных и отрисовка точек
inputData = fun.inputUser(points)
graph = fun.paintGraph(inputData, points)

# Если пользователь ввел одно число
if len(inputData) == 1:
    # Если ввели 0, то рисуем все графики
    if int(inputData[0]) == 0:
        # Пробегаемся по каждому набору координат отдельного графика
        for point in range(len(points)):
            graph = lagrange.getPolynomialLagrange(point[0], point[1], graph)
        graph.show()
    else:   # Иначе рисуем один график
        graph = lagrange.getPolynomialLagrange(points[int(inputData[0])-1][0], points[int(inputData[0])-1][1], graph)
        graph.show()
elif len(inputData) == 2:   # Если пользователь ввел диапозон
    # Записываем границы диапозона в переменные
    minValue = int(inputData[0])-1
    maxValue = int(inputData[1])
    print(minValue, " ", maxValue)
    # Пробегаемся по каждому набору координат отдельного графика
    for point in range(minValue, maxValue):
        graph = lagrange.getPolynomialLagrange(points[point][0], points[point][1], graph)
    graph.show()
