# 2. Составить генератор (yield), который выводит из строки только цифры.
def digits_generator(s):
    for ch in s:
        if ch.isdigit():
            yield ch
            
s = "g42sdgd34"

gen = digits_generator(s)

for x in gen:
    print(x)
