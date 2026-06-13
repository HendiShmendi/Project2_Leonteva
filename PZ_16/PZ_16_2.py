# 25. Создайте класс "Автомобиль", который содержит информацию о марке, модели и
# годе выпуска. Создайте класс "Грузовик", который наследуется от класса
# "Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
# "Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
# информацию о количестве пассажиров.
class Avtomobil:
    """Базовый класс, представляющий автомобиль."""

    def __init__(self, marka: str, model: str, god_vypuska: int):
        """Инициализация общих атрибутов автомобиля."""
        self.marka = marka
        self.model = model
        self.god_vypuska = god_vypuska

    def info(self) -> str:
        """Возвращает базовую информацию об автомобиле."""
        return (
            f"Марка: {self.marka}, "
            f"Модель: {self.model}, "
            f"Год выпуска: {self.god_vypuska}"
        )


class Gruzovick(Avtomobil):
    """Класс грузовика, наследуется от Avtomobil."""

    def __init__(
        self,
        marka: str,
        model: str,
        god_vypuska: int,
        gruzopodyomnost: float
    ):
        """Инициализация грузовика с грузоподъёмностью."""
        super().__init__(marka, model, god_vypuska)
        self.gruzopodyomnost = gruzopodyomnost  # в тоннах

    def info(self) -> str:
        """Возвращает информацию о грузовике."""
        return (
            f"{super().info()}, "
            f"Грузоподъёмность: {self.gruzopodyomnost} т"
        )


class LegkovoyAvtomobil(Avtomobil):
    """Класс легкового автомобиля, наследуется от Avtomobil."""

    def __init__(
        self,
        marka: str,
        model: str,
        god_vypuska: int,
        kolichestvo_passazhirov: int
    ):
        """Инициализация легкового авто с количеством пассажиров."""
        super().__init__(marka, model, god_vypuska)
        self.kolichestvo_passazhirov = kolichestvo_passazhirov

    def info(self) -> str:
        """Возвращает информацию о легковом автомобиле."""
        return (
            f"{super().info()}, "
            f"Количество пассажиров: {self.kolichestvo_passazhirov}"
        )


# Тестовые запуски
if __name__ == "__main__":
    # Базовый автомобиль
    avto = Avtomobil("Ford", "Focus", 2019)
    print(avto.info())

    # Грузовик
    gruz1 = Gruzovick("KAMAZ", "65115", 2021, 15.0)
    print(gruz1.info())

    gruz2 = Gruzovick("Volvo", "FH16", 2020, 25.5)
    print(gruz2.info())

    # Легковой автомобиль
    legk1 = LegkovoyAvtomobil("Toyota", "Corolla", 2022, 5)
    print(legk1.info())

    legk2 = LegkovoyAvtomobil("Hyundai", "Solaris", 2021, 5)
    print(legk2.info())