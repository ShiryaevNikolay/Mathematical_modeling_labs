import xlrd
import pandas as pd
import matplotlib.pyplot as plt

# Путь к файлу с данными
dataFilePath = (r"C:\Users\deend\Desktop\Мат. моделирование\lab_1\data_points_3.xlsx")

# Открываем файл
data = xlrd.open_workbook(dataFilePath, on_demand=True)

# Получаем количество листов в таблице
lists = len(data.sheet_names())

# Функция для получения точек для одного из графиков
def getData(sheet):
    # Инициализируем массивы для хнанения координат
    x = []
    y = []
    # Пробегаемся по каждой строке в файле с данными
    for rownum in range(sheet.nrows):
        # Записываем в массивы координаты X и Y из соответствующих столбцов
        x.append(sheet.cell(rownum, 0).value)
        y.append(sheet.cell(rownum, 1).value)
    # Возвращаем координаты для одного из графиков
    return [x, y]

# Функция рисование графиков
def paintGraph(inputData, points):
    # Если пользователь ввел одно число
    if len(inputData) == 1:
        # Если ввели 0, то рисуем все графики
        if int(inputData[0]) == 0:
            # Пробегаемся по каждому набору координат отдельного графика
            for point in range(len(points)):
                # Создаем таблицу координат
                df1 = pd.DataFrame({"x1": points[point][0], "y": points[point][1]})
                # Выводим в консоль для наглядности
                print(df1)
                # Строим график для текущего набора координат
                plt.scatter(df1["x1"], df1["y"])
            plt.show()
        else:   # Иначе рисуем один график
            # Создаем таблицу координат
            df1 = pd.DataFrame({"x1": points[int(inputData[0])-1][0], "y": points[int(inputData[0])-1][1]})
            # Выводим в консоль для наглядности
            print(df1)
            # Строим график для текущего набора координат
            plt.scatter(df1["x1"], df1["y"])
            plt.show()
    elif len(inputData) == 2:   # Если пользователь ввел диапозон
        # Записываем границы диапозона в переменные
        minValue = int(inputData[0])-1
        maxValue = int(inputData[1])
        print(minValue, " ", maxValue)
        # Пробегаемся по каждому набору координат отдельного графика
        for point in range(minValue, maxValue):
            # Создаем таблицу координат
            df1 = pd.DataFrame({"x1": points[point][0], "y": points[point][1]})
            # Выводим в консоль для наглядности
            print(df1)
            # Строим график для текущего набора координат
            plt.scatter(df1["x1"], df1["y"])
        plt.show()

# Функция запроса пользовательского ввода
def inputUser(points):
    # Колличество найденный графиков
    n = len(points)
    # Информация для пользователя
    print(f"Найдено графиков: {n}\n"
          f"Введите диапозон или определенный график, который нужно отрисовывать\n"
          f"Напрмер: 3 или 1-4. Для вывода всех графиков введите 0 или {n}")
    # Тут будут храниться введенные данные
    # Запрашиваем ввод, пока пользователь не введет корректные данные
    while True:
        # Запрашиваем ввод
        inputData = input("").split("-")
        # Нужно для проверки ввода
        correctInput = False
        # Проверяем все введенные данные
        for i in inputData:
            # try для проверки, друг была введена строка
            try:
                # Если число не выходит за диапозон количесва графиков
                if 0 < int(i) <= n:
                    correctInput = True
                # Если введена цифра 0
                elif len(inputData) == 1 and int(inputData[0]) == 0:
                    correctInput = True
                else:   # Иначе ввденые данные неверные
                    correctInput = False
                    break
            except:
                correctInput = False
                break
        # Если все введено правильно, то выходим из цикла
        if correctInput:
            break
        else:   # Иначе предупреждаем пользователя и запрашиваем ввод повторно
            print(f"Некорректный ввод. Попробуйте ещё раз")
    # Рисуем графики
    paintGraph(inputData, points)

# Функция для чтения данных из каждого листа и постоения соответствующих графиков
def showGraph(lists):
    # Инициализируем массив с координатами для всех графиков
    points = []
    # Пробегаемся во всем листам и записываем координаты в массив points
    for sheet in range(lists):
        points.append(getData(data.sheet_by_index(sheet)))
    # Запрашиваем пользовательский ввод
    inputUser(points)

# Запускаем код
showGraph(lists)
