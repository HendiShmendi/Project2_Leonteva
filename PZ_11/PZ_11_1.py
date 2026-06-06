# Создать список A на 10 случайных элементов. Создать список B из чисел A,
# меньших 0 и кратных 5. Найти количество чисел списка B. 

from random import randint

s = int(input("Введите начало диапазона(отрицательные): "))
e = int(input("Введите конец диапазона: "))
x = int(input("Сколько чисел сгенерировать: "))

A = [randint(s, e) for _ in range(x)]
B = list(filter(lambda number: number < 0 and number % 5 == 0, A))

print("Список A:", A)
print("Список B:", B)
print("Количество чисел в списке B:", len(B))
