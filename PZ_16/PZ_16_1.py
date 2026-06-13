# Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
# Напишите метод, который выводит информацию о машине в формате "Марка:
# марка, Модель: модель, Год выпуска: год".
class Mashina:
    """Класс, представляющий автомобиль."""

    def __init__(self, marka: str, model: str, god_vypuska: int):
        """Инициализация атрибутов машины."""
        self.marka = marka
        self.model = model
        self.god_vypuska = god_vypuska

    def info(self) -> str:
        """Возвращает информацию о машине."""
        return (
            f"Марка: {self.marka}, "
            f"Модель: {self.model}, "
            f"Год выпуска: {self.god_vypuska}"
        )


# Тестовые запуски
if __name__ == "__main__":
    car1 = Mashina("Toyota", "Camry", 2020)
    print(car1.info())

    car2 = Mashina("BMW", "X5", 2018)
    print(car2.info())

    car3 = Mashina("Lada", "Vesta", 2022)
    print(car3.info())