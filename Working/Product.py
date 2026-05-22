class Product:
    """Класс для представления товара в нашей системе"""

    def __init__(self, product_id: int, name: str, purchase_price: float, retail_price: float) -> None:
        """Инициализация товара с проверками прямо при создании

        Args:
            product_id (int): айди товара
            name (str): название товара
            purchase_price (float): цена закупки у поставщика
            retail_price (float): цена по которой будем продавать

        Raises:
            TypeError: если передали неправильный тип данных
            ValueError: если передали пустую строку или отрицательные числа
        """

        if not isinstance(product_id, int):
            raise TypeError("айди товара должен быть целым числом")

        if not isinstance(name, str):
            raise TypeError("название должно быть обычным текстом")

        if not name or not name.strip():
            raise ValueError("название товара не может быть пустым")

        if not isinstance(purchase_price, (int, float)):
            raise TypeError("цена закупки должна быть цифрой")

        if purchase_price < 0:
            raise ValueError("цена закупки не может уходить в минус")

        if not isinstance(retail_price, (int, float)):
            raise TypeError("розничная цена должна быть цифрой")

        if retail_price < 0:
            raise ValueError("розничная цена не может быть отрицательной")

        self.product_id = product_id
        self.name = name.strip()
        self.purchase_price = float(purchase_price)
        self.retail_price = float(retail_price)

    def get_info(self) -> str:
        """Метод чтобы получить информацию по товару

        Returns:
            str: готовая строка с данными товара
        """

        info = f"[Товар ID: {self.product_id}] {self.name}, закупка: {self.purchase_price}, розница: {self.retail_price}"

        return info
