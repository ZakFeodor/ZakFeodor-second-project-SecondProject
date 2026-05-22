from abc import ABC, abstractmethod


class Facility(ABC):
    """Базовый абстрактный класс для обьектов типа складов и магазинов"""

    def __init__(self, facility_id: int, name: str, address: str, manager_id: int = None) -> None:
        """Задаем базовые параметры для любого здания или точки

        Args:
            facility_id (int): айди обьекта
            name (str): как называется точка
            address (str): физический адрес
            manager_id (int, optional): айди ответственного работника

        Raises:
            TypeError: если типы данных не те
            ValueError: если строки пустые
        """

        if not isinstance(facility_id, int):
            raise TypeError("айди обьекта должен быть целым числом")

        if not isinstance(name, str):
            raise TypeError("название обьекта должно быть текстом")

        if not name or not name.strip():
            raise ValueError("название не может быть пустым")

        if not isinstance(address, str):
            raise TypeError("адрес тоже должен быть текстом")

        if not address or not address.strip():
            raise ValueError("нужно указать нормальный адрес а не пустоту")

        if manager_id is not None and not isinstance(manager_id, int):
            raise TypeError("айди менеджера должно быть числом или его вообще не должно быть")

        self.facility_id = facility_id
        self.name = name.strip()
        self.address = address.strip()
        self.manager_id = manager_id

    def change_manager(self, new_manager_id: int) -> None:
        """Меняет ответственное лицо на обьекте

        Args:
            new_manager_id (int): айди нового ответственного сотрудника

        Raises:
            TypeError: если передали не число
        """

        if not isinstance(new_manager_id, int):
            raise TypeError("айди нового менеджера должно быть целым числом")

        self.manager_id = new_manager_id

    @abstractmethod
    def get_inventory_info(self) -> str:
        """Метод который потом надо будет переопределить для складов

        Returns:
            str: информация по остаткам
        """
        pass
