# Напиши программу на Python,которая считывает текстовый файл с именем "html.txt", ищет в нём все html-теги и выводит их в консоль,каждыйьна новой строке.Если файл не существует или не содержит html-тегов,вывести соответствующее сообщение.
import re

try:  
    with open("html.txt", "r", encoding="utf-8") as file:
        content = file.read()
        tags = re.findall(r'<[^>]+>', content)
        if tags:
            print("Найденные HTML-теги:")
            for tag in tags:
                print(tag)
        else:
            print("В файле нет HTML-тегов.")
except FileNotFoundError:
    print("Файл 'html.txt' не найден.")
    