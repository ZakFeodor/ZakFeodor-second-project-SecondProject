from abc import ABC, abstractmethod


class Person(ABC):
    """Абстрактный базовый класс для всех людей в CRM-системе.

    Служит основой для классов Employee (Работник) и Customer (Покупатель).
    Реализует инкапсуляцию базовых данных (ID, имя, телефон) и
    задает обязательный контракт (абстрактный метод) для дочерних классов.
    """

    def __init__(self, person_id: int, name: str, phone: str) -> None:
        """Инициализация базовых атрибутов человека.

        Args:
            person_id (int): Уникальный идентификатор человека в системе.
            name (str): ФИО или имя человека.
            phone (str): Контактный номер телефона.

        Raises:
            TypeError: Если типы переданных аргументов не совпадают с ожидаемыми.
            ValueError: Если переданы логически некорректные значения.
        """

        if not isinstance(person_id, int):
            raise TypeError("ID человека должен быть целым числом.")

        self._person_id = person_id
        self.name = name
        self.phone = phone

    @property
    def person_id(self) -> int:
        """int: Возвращает уникальный идентификатор (read-only)."""

        return self._person_id

    @property
    def name(self) -> str:
        """str: Возвращает имя человека."""

        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает имя с предварительной проверкой.

        Args:
            value (str): Новое имя.

        Raises:
            TypeError: Если переданное значение не является строкой.
            ValueError: Если передана пустая строка или строка из пробелов.
        """

        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой.")

        if not value or not value.strip():
            raise ValueError("Имя человека не может быть пустым.")

        self._name = value.strip()

    @property
    def phone(self) -> str:
        """str: Возвращает номер телефона."""

        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        """Устанавливает номер телефона с базовой проверкой.

        Args:
            value (str): Новый номер телефона.

        Raises:
            TypeError: Если переданное значение не является строкой.
            ValueError: Если номер телефона слишком короткий.
        """

        if not isinstance(value, str):
            raise TypeError("Номер телефона должен быть строкой.")

        clean_phone = value.strip()

        if len(clean_phone) < 5:
            raise ValueError("Номер телефона должен содержать минимум 5 символов.")

        self._phone = clean_phone

    @abstractmethod
    def get_info(self) -> str:
        """Абстрактный метод для получения сводной информации о человеке.

        Обеспечивает полиморфизм: каждый дочерний класс обязан
        переопределить этот метод и возвращать информацию в своем формате.

        Returns:
            str: Строка с отформатированной информацией.
        """

        pass
