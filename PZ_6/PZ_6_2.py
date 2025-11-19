# 2.
# Даны два списка А и В одинакового размера N. Сформировать новый список С того
# же размера, каждый элемент которого равен максимальному из элементов списков
# А и В.
import random

N = int(input('Введите размер списков N: '))

A = []
B = []
i = 0

# Заполняем списки A и B случайными числами
while i < N:
    A.append(random.randint(0, 100))
    B.append(random.randint(0,100))
    i += 1

print('Список A:', A)
print('Список B:', B)

# Формируем список C
C = []
i = 0
while i < N:
    if A[i] > B[i]:
        C.append(A[i])
    else:
        C.append(B[i])
    i += 1

print('Список C', C)

