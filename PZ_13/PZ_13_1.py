# 25. В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов.
import re

# Читаем файл
with open("Dostoevsky.txt", encoding="utf-8") as f:
    text = f.read()

# Находим все произведения — текст в кавычках «», 
works = re.findall(r'«([А-ЯЁA-Z][^»]+)»', text)

# Убираем дубликаты, сохраняя порядок
unique_works = list(dict.fromkeys(works))

print("Произведения Достоевского:")
list(map(lambda i_w: print(f"  {i_w[0] + 1}. {i_w[1]}"), enumerate(unique_works)))

print(f"\nВсего найдено произведений (с повторами): {len(works)}")
print(f"Уникальных произведений: {len(unique_works)}")