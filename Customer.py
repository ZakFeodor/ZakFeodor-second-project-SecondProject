from Person import Person


class Customer(Person):
    """Класс покупателя (клиента компании).

    Наследует базовые атрибуты от Person и хранит общую сумму,
    которую покупатель потратил в компании.
    """

    def __init__(self, person_id: int, name: str, phone: str, total_spent: float = 0.0) -> None:
        """Инициализация атрибутов покупателя.

        Args:
            person_id (int): Уникальный идентификатор покупателя.
            name (str): Имя покупателя.
            phone (str): Контактный телефон.
            total_spent (float, optional): Общая сумма покупок. По умолчанию 0.0.

        Raises:
            TypeError: Если типы переданных аргументов не совпадают с ожидаемыми.
            ValueError: Если переданы некорректные значения.
        """

        super().__init__(person_id, name, phone)
        self.total_spent = total_spent

    @property
    def total_spent(self) -> float:
        """
        Returns:
            float: Возвращает общую сумму трат покупателя.
        """

        return self._total_spent

    @total_spent.setter
    def total_spent(self, value: float) -> None:
        """Устанавливает общую сумму трат с проверкой.

        Args:
            value (float): Новая сумма трат.

        Raises:
            TypeError: Если значение не является числом.
            ValueError: Если сумма меньше нуля.
        """

        if not isinstance(value, (int, float)):
            raise TypeError("Сумма трат должна быть числом.")

        if value < 0:
            raise ValueError("Сумма трат не может быть отрицательной.")

        self._total_spent = float(value)

    def add_purchase_amount(self, amount: float) -> None:
        """Увеличивает общую сумму трат покупателя на указанную величину.

        Args:
            amount (float): Сумма новой покупки.

        Raises:
            TypeError: Если передано не число.
            ValueError: Если сумма покупки меньше или равна нулю.
        """

        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма покупки должна быть числом.")

        if amount <= 0:
            raise ValueError("Сумма покупки должна быть больше нуля.")

        self.total_spent += float(amount)

    def get_info(self) -> str:
        """Получает сводную информацию о покупателе.

        Returns:
            str: Форматированная строка с данными покупателя.
        """

        info_string = f"[Покупатель ID: {self.person_id}] {self.name} | Тел: {self.phone} | Потрачено всего: {self.total_spent:.2f} руб."

        return info_string
