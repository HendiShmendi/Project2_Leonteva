# В матрице найти сумму элементов второй половины матрицы.
import random

# Пользователь сам вводит размер матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Создаём матрицу со случайными числами
matrix = [[random.randint(-10, 10) for j in range(cols)] for i in range(rows)]

print("\nИсходная матрица:")
for row in matrix:
    print(row)

# Находим границу второй половины
half = cols // 2

# Считаем сумму второй половины
total = 0
for i in range(rows):
    for j in range(half, cols):
        total += matrix[i][j]

print(f"\nВторая половина (столбцы с {half} по {cols-1}):")
for row in matrix:
    print(row[half:])

print(f"\nСумма элементов второй половины: {total}")
