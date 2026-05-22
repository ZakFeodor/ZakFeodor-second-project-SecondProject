from datetime import datetime


class Order:
    """Класс для фиксации любых движений товаров и денег в системе"""

    def __init__(self, order_id: int, order_type: str, product_id: int, quantity: int, total_amount: float,
                 customer_id: int = None) -> None:
        """Создает запись о заказе или операции

        Args:
            order_id (int): номер заказа
            order_type (str): тип операции типа покупка продажа или возврат
            product_id (int): айди товара
            quantity (int): количество товара
            total_amount (float): итоговая сумма операции
            customer_id (int, optional): айди клиента если это продажа

        Raises:
            TypeError: если передали кривые типы данных
            ValueError: если числа отрицательные или строки пустые
        """

        if not isinstance(order_id, int):
            raise TypeError("номер заказа должен быть целым числом")

        if not isinstance(order_type, str):
            raise TypeError("тип заказа должен быть обычным текстом")

        if not order_type or not order_type.strip():
            raise ValueError("тип заказа не может быть пустым")

        if not isinstance(product_id, int):
            raise TypeError("айди товара должно быть числом")

        if not isinstance(quantity, int):
            raise TypeError("количество должно быть целым числом")

        if quantity <= 0:
            raise ValueError("количество в заказе должно быть больше нуля")

        if not isinstance(total_amount, (int, float)):
            raise TypeError("сумма заказа должна быть цифрой")

        if total_amount < 0:
            raise ValueError("сумма заказа не может уходить в минус")

        if customer_id is not None and not isinstance(customer_id, int):
            raise TypeError("айди клиента должно быть числом или отсутствовать")

        self.order_id = order_id
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.order_type = order_type.strip()
        self.product_id = product_id
        self.quantity = quantity
        self.total_amount = float(total_amount)
        self.customer_id = customer_id

    def get_info(self) -> str:
        """Возвращает чек или информацию по заказу

        Returns:
            str: текст с данными заказа
        """

        client_info = f"Клиент: {self.customer_id}" if self.customer_id else "Внутренняя операция"
        info = f'''[{self.date}] Заказ {self.order_id}  Тип: {self.order_type}  
        Товар ID {self.product_id}  {self.quantity} шт  Сумма: {self.total_amount}  {client_info}'''

        return info
