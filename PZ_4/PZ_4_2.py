# 2. Дано целое число N (>0). Если оно является степенью числа 3, то вывести TRUE,если не является - вывести FALSE.

try:
    N = int(input("Введите целое число N (>0): "))
    if N <= 0:
        print("Ошибка: число должно быть больше 0!")
    else:
        x = N
        while x % 3 == 0:
            x //= 3
        if x == 1:
            print("TRUE")
        else:
            print("FALSE")
except ValueError:
    print("Ошибка: введите целое число!")   