from Facility import Facility


class PointOfSale(Facility):
    """Класс розничной точки продаж или магазина"""

    def __init__(self, facility_id: int, name: str, address: str, manager_id: int = None) -> None:
        """Создает точку продаж

        Args:
            facility_id (int): айди магазина
            name (str): название магазина
            address (str): адрес
            manager_id (int, optional): айди директора магазина
        """

        super().__init__(facility_id, name, address, manager_id)
        self.inventory = {}
        self.revenue = 0.0

    def receive_products(self, product_id: int, count: int) -> None:
        """Принимает товар на баланс магазина

        Args:
            product_id (int): айди товара
            count (int): количество которое привезли

        Raises:
            TypeError: если передали не числа
            ValueError: если количество в минусе
        """

        if not isinstance(product_id, int):
            raise TypeError("айди товара должен быть целым числом")

        if not isinstance(count, int):
            raise TypeError("количество должно быть целым числом")

        if count <= 0:
            raise ValueError("количество для приемки должно быть больше нуля")

        if product_id in self.inventory:
            self.inventory[product_id] += count
        else:
            self.inventory[product_id] = count

    def sell_product(self, product_id: int, count: int, price: float) -> None:
        """Списывает товар из наличия и прибавляет деньги к выручке

        Args:
            product_id (int): какой товар продаем
            count (int): сколько штук
            price (float): по какой цене продаем каждую штуку

        Raises:
            TypeError: если количество не число
            ValueError: если товара не хватает на точке
        """

        if not isinstance(count, int):
            raise TypeError("количество на продажу должно быть целым числом")

        if count <= 0:
            raise ValueError("нельзя продать ноль или меньше товаров")

        if product_id not in self.inventory or self.inventory[product_id] < count:
            raise ValueError("на точке нет такого количества этого товара")

        self.inventory[product_id] -= count
        self.revenue += (count * price)

        if self.inventory[product_id] == 0:
            del self.inventory[product_id]

    def get_inventory_info(self) -> str:
        """Выдает список остатков товаров на точке

        Returns:
            str: текст с остатками и выручкой
        """

        lines = [f"Точка продаж: {self.name}б Текущая выручка: {self.revenue} руб "]

        if not self.inventory:
            lines.append("Товаров в наличии нет")
        else:
            for prod_id, count in self.inventory.items():
                lines.append(f"Товар ID {prod_id}: {count} шт")

        info = "\n".join(lines)

        return info
    