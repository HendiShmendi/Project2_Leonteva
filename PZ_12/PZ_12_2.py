# В матрице элементы второго столбца возвести в квадрат.
import random

# Пользователь сам вводит размер матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Проверка — должно быть минимум 2 столбца
if cols < 2:
    print("Ошибка: должно быть минимум 2 столбца!")
else:
    # Создаём матрицу со случайными числами (генератор списков)
    matrix = [[random.randint(-5, 5) for j in range(cols)] for i in range(rows)]

    print("\nИсходная матрица:")
    list(map(print, matrix))

    # Возводим второй столбец (индекс 1) в квадрат через map + lambda
    # Для каждой строки: элемент с индексом 1 заменяется на его квадрат
    result = list(map(
        lambda row: [val ** 2 if idx == 1 else val for idx, val in enumerate(row)],
        matrix
    ))

    print("\nМатрица после возведения второго столбца в квадрат:")
    list(map(print, result))