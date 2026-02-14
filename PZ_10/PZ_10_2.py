# 2.
# Из предложенного текстового файла (text18-25. txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно удалив букву «с» из текста

input_path = "text18-25.txt"
output_path = "poem_without_s.txt"

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

print("Содержимое файла:\n")
print(text)

# Количество символов всего (включая пробелы и переносы)
total_chars = len(text)

# Количество символов, которые являются буквами
letters_count = sum(1 for ch in text if ch.isalpha())

print("\nКоличество символов всего:", total_chars)
print("Количество символов-букв:", letters_count)

# Удаляем 'с' и 'С'
new_text = text.replace("с", "").replace("С", "")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(new_text)

print("\nНовый файл создан:", output_path)
