# В матрице элементы второго столбца возвести в квадрат.
import random

# Пользователь сам вводит размер матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Проверка — должно быть минимум 2 столбца
if cols < 2:
    print("Ошибка: должно быть минимум 2 столбца!")
else:
    # Создаём матрицу со случайными числами
    matrix = [[random.randint(-5, 5) for j in range(cols)] for i in range(rows)]

    print("\nИсходная матрица:")
    for row in matrix:
        print(row)

    # Возводим второй столбец (индекс 1) в квадрат
    for i in range(rows):
        matrix[i][1] = matrix[i][1] ** 2

    print("\nМатрица после возведения второго столбца в квадрат:")
    for row in matrix:
        print(row)