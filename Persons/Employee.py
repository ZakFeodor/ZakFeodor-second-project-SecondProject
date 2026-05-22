from Person import Person


class Employee(Person):
    """Класс работника компании.

    Наследует базовые атрибуты от Person и добавляет специфичные для
    работника данные: должность, зарплату и ID места работы.
    """

    def __init__(self, person_id: int, name: str, phone: str, position: str, salary: float,
                 assigned_facility_id: int = None) -> None:
        """Инициализация атрибутов работника.

        Args:
            person_id (int): Уникальный идентификатор работника.
            name (str): ФИО работника.
            phone (str): Контактный телефон.
            position (str): Должность.
            salary (float): Заработная плата.
            assigned_facility_id (int, optional): ID склада или пункта продаж. По умолчанию None.

        Raises:
            TypeError: Если типы переданных аргументов не совпадают с ожидаемыми.
            ValueError: Если переданы некорректные значения.
        """

        super().__init__(person_id, name, phone)
        self.position = position
        self.salary = salary
        self.assigned_facility_id = assigned_facility_id

    @property
    def position(self) -> str:
        """
        Returns:
            str: Возвращает должность работника.
        """

        return self._position

    @position.setter
    def position(self, value: str) -> None:
        """Устанавливает должность работника с проверкой.

        Args:
            value (str): Новая должность.

        Raises:
            TypeError: Если переданное значение не является строкой.
            ValueError: Если передана пустая строка.
        """

        if not isinstance(value, str):
            raise TypeError("Должность должна быть строкой.")

        if not value or not value.strip():
            raise ValueError("Должность не может быть пустой.")

        self._position = value.strip()

    @property
    def salary(self) -> float:
        """
        Returns:
            float: Возвращает размер заработной платы.
        """

        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """Устанавливает размер зарплаты с проверкой.

        Args:
            value (float): Новая зарплата.

        Raises:
            TypeError: Если значение не является числом.
            ValueError: Если зарплата меньше нуля.
        """

        if not isinstance(value, (int, float)):
            raise TypeError("Зарплата должна быть числом.")

        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной.")

        self._salary = float(value)

    @property
    def assigned_facility_id(self) -> int:
        """
        Returns:
            int: Возвращает ID объекта (склада/пункта продаж), за которым закреплен работник.
        """

        return self._assigned_facility_id

    @assigned_facility_id.setter
    def assigned_facility_id(self, value: int) -> None:
        """Устанавливает ID объекта для работника.

        Args:
            value (int): ID объекта или None, если работник пока никуда не назначен.

        Raises:
            TypeError: Если значение не является целым числом или None.
        """

        if value is not None and not isinstance(value, int):
            raise TypeError("ID объекта должен быть целым числом или None.")

        self._assigned_facility_id = value

    def get_info(self) -> str:
        """Получает сводную информацию о работнике.

        Returns:
            str: Форматированная строка с данными работника.
        """

        facility_info = str(self.assigned_facility_id) if self.assigned_facility_id is not None else "Не назначен"
        info_string = (f'''[Работник ID: {self.person_id}] {self.name}, Тел: {self.phone}, Должность: {self.position}, "
                       ЗП: {self.salary},  Объект: {facility_info}''')

        return info_string
