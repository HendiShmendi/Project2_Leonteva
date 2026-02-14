# Вариант 25.
# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (. txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Элементы после сортировки:
# Количество элементов:
# Минимальный элемент кратный 2:
# Максимальный элемент кратный 5:


file1 = "nums1.txt"
file2 = "nums2.txt"
result_file = "result_task1.txt"

# Формируем два файла с числами (пример последовательностей)
nums1 = [10, -3, 7, -8, 12, -15]
nums2 = [-20, 5, -1, 14, -6, 25]

with open(file1, "w", encoding="utf-8") as f:
    f.write(" ".join(map(str, nums1)))

with open(file2, "w", encoding="utf-8") as f:
    f.write(" ".join(map(str, nums2)))

# Читаем числа из файлов
def read_numbers(path: str) -> list[int]:
    with open(path, "r", encoding="utf-8") as f:
        return list(map(int, f.read().split()))

a = read_numbers(file1)
b = read_numbers(file2)

# Обработка
all_nums = a + b
sorted_nums = sorted(all_nums)
count_nums = len(all_nums)

evens = [x for x in all_nums if x % 2 == 0]
min_even = min(evens) if evens else "не найден"

fives = [x for x in all_nums if x % 5 == 0]
max_five = max(fives) if fives else "не найден"

# Запись результата
with open(result_file, "w", encoding="utf-8") as f:
    f.write("Элементы первого и второго файлов:\n")
    f.write(f"Файл 1: {a}\n")
    f.write(f"Файл 2: {b}\n\n")

    f.write("Элементы после сортировки:\n")
    f.write(f"{sorted_nums}\n\n")

    f.write(f"Количество элементов: {count_nums}\n")
    f.write(f"Минимальный элемент кратный 2: {min_even}\n")
    f.write(f"Максимальный элемент кратный 5: {max_five}\n")

print("Задание 1 выполнено. Результат записан в", result_file)

