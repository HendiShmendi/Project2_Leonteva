# 1. Дана последовательность целых чисел. Поменять местами ее первую и
# последнюю трети.
swap = lambda s: ' '.join(
    (lambda a, n: a[-n:] + a[n:-n] + a[:n] if n > 0 else a)(s.split(), len(s.split()) // 3)
)

s = "1 2 3 4 5 6 7 8 "
print(swap(s))