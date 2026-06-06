# В матрице найти сумму элементов второй половины матрицы.
import random
from functools import reduce

# Пользователь сам вводит размер матрицы
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Создаём матрицу со случайными числами (генератор списков)
matrix = [[random.randint(-10, 10) for j in range(cols)] for i in range(rows)]

print("\nИсходная матрица:")
list(map(print, matrix))

# Находим границу второй половины
half = cols // 2

# Извлекаем вторую половину каждой строки через map + lambda
second_half = list(map(lambda row: row[half:], matrix))

# Считаем сумму через reduce + map: сначала суммируем каждую строку, потом складываем
total = reduce(lambda acc, row: acc + reduce(lambda a, b: a + b, row), second_half, 0)

print(f"\nВторая половина (столбцы с {half} по {cols - 1}):")
list(map(print, second_half))

print(f"\nСумма элементов второй половины: {total}")
