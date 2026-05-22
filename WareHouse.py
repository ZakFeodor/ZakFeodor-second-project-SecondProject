from Facility import Facility
from Product import Product


class WarehouseCell:
    """Класс отдельной ячейки на складе для хранения конкретного товара"""

    def __init__(self, cell_id: int, capacity: int) -> None:
        """Создает пустую ячейку с указанной вместимостью

        Args:
            cell_id (int): порядковый номер ячейки
            capacity (int): сколько штук товара в нее влезет

        Raises:
            TypeError: если переданы не целые числа
            ValueError: если вместимость меньше или равна нулю
        """

        if not isinstance(cell_id, int):
            raise TypeError("айди ячейки должен быть целым числом")

        if not isinstance(capacity, int):
            raise TypeError("вместимость должна быть числом")

        if capacity <= 0:
            raise ValueError("вместимость ячейки должна быть больше нуля")

        self.cell_id = cell_id
        self.capacity = capacity
        self.product = None
        self.quantity = 0

    def add_items(self, product: Product, count: int) -> None:
        """Добавляет определенное количество товара в ячейку

        Args:
            product (Product): сам обьект товара который кладем
            count (int): сколько штук кладем

        Raises:
            TypeError: если количество не число
            ValueError: если товар другой или места не хватает
        """

        if not isinstance(count, int):
            raise TypeError("количество товара должно быть целым числом")

        if count <= 0:
            raise ValueError("нельзя положить отрицательное количество товара")

        if self.product is not None and self.product.product_id != product.product_id:
            raise ValueError("в этой ячейке уже лежит другой товар")

        if self.quantity + count > self.capacity:
            raise ValueError("в ячейке не хватает места для такого количества")

        self.product = product
        self.quantity += count

    def remove_items(self, count: int) -> None:
        """Забирает часть товара из ячейки

        Args:
            count (int): сколько штук забираем

        Raises:
            TypeError: если количество не число
            ValueError: если товара не хватает или число кривое
        """

        if not isinstance(count, int):
            raise TypeError("количество для изьятия должно быть числом")

        if count <= 0:
            raise ValueError("нельзя забрать нулевое или отрицательное количество")

        if self.quantity < count:
            raise ValueError("в ячейке нет столько товара")

        self.quantity -= count

        if self.quantity == 0:
            self.product = None


class Warehouse(Facility):
    """Класс склада который состоит из множества ячеек"""

    def __init__(self, facility_id: int, name: str, address: str, manager_id: int = None) -> None:
        """Создает склад на базе родительского класса

        Args:
            facility_id (int): айди склада
            name (str): название склада
            address (str): адрес
            manager_id (int, optional): айди начальника склада
        """

        super().__init__(facility_id, name, address, manager_id)
        self.cells = []
        self._next_cell_id = 1

    def add_cell(self, capacity: int) -> None:
        """Добавляет новую пустую ячейку на склад

        Args:
            capacity (int): вместимость новой ячейки
        """

        new_cell = WarehouseCell(self._next_cell_id, capacity)
        self.cells.append(new_cell)
        self._next_cell_id += 1

    def get_inventory_info(self) -> str:
        """Собирает информацию по всем ячейкам склада

        Returns:
            str: список всех ячеек и что в них лежит
        """

        lines = [f"Склад: {self.name}"]

        for cell in self.cells:
            if cell.product:
                lines.append(f"Ячейка {cell.cell_id}: {cell.product.name} - {cell.quantity} шт из {cell.capacity}")
            else:
                lines.append(f"Ячейка {cell.cell_id}: пустая (вместимость {cell.capacity})")

        info = "\n".join(lines)

        return info
