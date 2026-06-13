# Приложение ПЛАТНАЯ ПОЛИКЛИНИКА для некоторой организации. БД
# должна содержать таблицу Пациент со следующей структурой записи: ФИО пациента,
# ФИО врача, диагноз, стоимость лечение.

import sqlite3 as sq

with sq.connect('clinic.db') as con:
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Patient (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio_patient TEXT NOT NULL,
            fio_doctor TEXT NOT NULL,
            diagnosis TEXT NOT NULL,
            cost REAL NOT NULL
        )
    """)

    cur.execute("DELETE FROM Patient")

    patients_data = [
        (1,  'Иванов И.И.',    'Петров С.Н.',    'ОРВИ',            1500),
        (2,  'Сидорова М.П.',  'Кузнецова А.В.', 'Гастрит',         3200),
        (3,  'Козлов Д.А.',    'Петров С.Н.',    'Гипертония',      4800),
        (4,  'Новикова О.С.',  'Романов И.П.',   'Сахарный диабет', 7500),
        (5,  'Морозов А.Ю.',   'Кузнецова А.В.', 'Бронхит',         2100),
        (6,  'Волкова Н.И.',   'Романов И.П.',   'Артрит',          5600),
        (7,  'Соколов П.Д.',   'Петров С.Н.',    'Аллергия',        1800),
        (8,  'Лебедева В.А.',  'Захарова Е.М.',  'Мигрень',         3900),
        (9,  'Попов Р.В.',     'Захарова Е.М.',  'Остеохондроз',    4200),
        (10, 'Семёнова И.О.',  'Кузнецова А.В.', 'Пневмония',       8500),
    ]

    cur.executemany(
        "INSERT INTO Patient (id, fio_patient, fio_doctor, diagnosis, cost) VALUES (?, ?, ?, ?, ?)",
        patients_data
    )

    print("Добавлено 10 записей.\n")

print("--- ПОИСК ---")

with sq.connect('clinic.db') as con:
    cur = con.cursor()

    print("1 - поиск по ФИО пациента")
    print("2 - поиск по ФИО врача и стоимости лечения >= заданной")
    print("3 - поиск по диагнозу")
    choice = input("Выберите вариант: ")

    if choice == '1':
        fio = input("Введите ФИО пациента: ")
        cur.execute("SELECT * FROM Patient WHERE fio_patient = ?", (fio,))
        for row in cur.fetchall():
            print(row)

    elif choice == '2':
        doctor = input("Введите ФИО врача: ")
        min_cost = float(input("Минимальная стоимость лечения: "))
        cur.execute(
            "SELECT * FROM Patient WHERE fio_doctor = ? AND cost >= ?",
            (doctor, min_cost)
        )
        for row in cur.fetchall():
            print(row)

    elif choice == '3':
        diag = input("Введите диагноз: ")
        cur.execute("SELECT * FROM Patient WHERE diagnosis = ?", (diag,))
        for row in cur.fetchall():
            print(row)

    else:
        print("Неверный выбор")

print("\n--- УДАЛЕНИЕ ---")

with sq.connect('clinic.db') as con:
    cur = con.cursor()

    print("1 - удалить по id")
    print("2 - удалить по ФИО врача")
    print("3 - удалить со стоимостью лечения > N")
    choice = input("Выберите вариант: ")

    if choice == '1':
        uid = int(input("Введите id: "))
        cur.execute("DELETE FROM Patient WHERE id = ?", (uid,))
        print("Удалено записей:", cur.rowcount)

    elif choice == '2':
        doctor = input("Введите ФИО врача: ")
        cur.execute("DELETE FROM Patient WHERE fio_doctor = ?", (doctor,))
        print("Удалено записей:", cur.rowcount)

    elif choice == '3':
        max_cost = float(input("Стоимость лечения больше: "))
        cur.execute("DELETE FROM Patient WHERE cost > ?", (max_cost,))
        print("Удалено записей:", cur.rowcount)

    else:
        print("Неверный выбор")

print("\n--- РЕДАКТИРОВАНИЕ ---")

with sq.connect('clinic.db') as con:
    cur = con.cursor()

    print("1 - изменить диагноз по id")
    print("2 - изменить стоимость лечения по ФИО пациента")
    print("3 - изменить ФИО врача по диагнозу")
    choice = input("Выберите вариант: ")

    if choice == '1':
        uid = int(input("Введите id: "))
        new_diag = input("Новый диагноз: ")
        cur.execute("UPDATE Patient SET diagnosis = ? WHERE id = ?", (new_diag, uid))
        print("Обновлено записей:", cur.rowcount)

    elif choice == '2':
        fio = input("Введите ФИО пациента: ")
        new_cost = float(input("Новая стоимость лечения: "))
        cur.execute("UPDATE Patient SET cost = ? WHERE fio_patient = ?", (new_cost, fio))
        print("Обновлено записей:", cur.rowcount)

    elif choice == '3':
        diag = input("Введите диагноз: ")
        new_doctor = input("Новое ФИО врача: ")
        cur.execute("UPDATE Patient SET fio_doctor = ? WHERE diagnosis = ?", (new_doctor, diag))
        print("Обновлено записей:", cur.rowcount)

    else:
        print("Неверный выбор")

print("\n--- ВСЕ ЗАПИСИ ПОСЛЕ ИЗМЕНЕНИЙ ---")

with sq.connect('clinic.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Patient")
    for row in cur.fetchall():
        print(row)