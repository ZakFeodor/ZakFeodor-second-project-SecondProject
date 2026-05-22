from DataManager import DataManager
from ConsoleUI import ConsoleUI


def main() -> None:
    """Точка входа в нашу программу"""

    print("Пытаемся загрузить данные из файла")

    system = DataManager.load_data("my_company.json")
    ui = ConsoleUI(system)

    ui.start()

    print("Сохраняем данные перед выходом")

    DataManager.save_data(system, "my_company.json")

    print("Программа закрыта удачного дня")


if __name__ == "__main__":
    main()
