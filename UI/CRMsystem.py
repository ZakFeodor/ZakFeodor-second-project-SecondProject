from Employee import Employee
from Customer import Customer
from WareHouse import Warehouse
from PointOfSale import PointOfSale
from Product import Product
from Order import Order


class CrmSystem:
    """Главный класс который управляет всеми процессами в компании"""

    def __init__(self) -> None:
        """Инициализация пустых списков для хранения данных компании"""

        self.employees = []
        self.customers = []
        self.warehouses = []
        self.points_of_sale = []
        self.product_catalog = []
        self.orders = []
        self.company_budget = 100000.0
        self._next_order_id = 1

    def hire_employee(self, employee: Employee) -> None:
        """Нанимает нового работника в компанию

        Args:
            employee (Employee): обьект работника

        Raises:
            TypeError: если передали не работника
        """

        if not isinstance(employee, Employee):
            raise TypeError("в этот метод нужно передавать обьект работника")

        self.employees.append(employee)

    def open_warehouse(self, warehouse: Warehouse) -> None:
        """Открывает новый склад

        Args:
            warehouse (Warehouse): обьект склада

        Raises:
            TypeError: если передали не склад
        """

        if not isinstance(warehouse, Warehouse):
            raise TypeError("нужно передать обьект склада")

        self.warehouses.append(warehouse)

    def open_point_of_sale(self, pos: PointOfSale) -> None:
        """Открывает новую точку продаж

        Args:
            pos (PointOfSale): обьект магазина

        Raises:
            TypeError: если передали не точку продаж
        """

        if not isinstance(pos, PointOfSale):
            raise TypeError("ожидался обьект точки продаж")

        self.points_of_sale.append(pos)

    def add_product_to_catalog(self, product: Product) -> None:
        """Добавляет товар в общий каталог чтобы его можно было закупать

        Args:
            product (Product): обьект товара

        Raises:
            TypeError: если передали не товар
        """

        if not isinstance(product, Product):
            raise TypeError("нужно передать обьект товара")

        self.product_catalog.append(product)

    def purchase_products(self, product_id: int, warehouse_id: int, quantity: int) -> None:
        """Закупает товар у поставщика на склад

        Args:
            product_id (int): айди товара из каталога
            warehouse_id (int): на какой склад везем
            quantity (int): сколько штук покупаем

        Raises:
            ValueError: если не нашли товар или склад или нет денег
        """

        target_product = None

        for prod in self.product_catalog:
            if prod.product_id == product_id:
                target_product = prod
                break

        if not target_product:
            raise ValueError("такой товар не найден в каталоге")

        target_warehouse = None

        for wh in self.warehouses:
            if wh.facility_id == warehouse_id:
                target_warehouse = wh
                break

        if not target_warehouse:
            raise ValueError("склад с таким айди не найден")

        total_cost = target_product.purchase_price * quantity

        if self.company_budget < total_cost:
            raise ValueError("в бюджете компании не хватает бабок на закупку")

        placed = False

        for cell in target_warehouse.cells:
            if (cell.product is None or cell.product.product_id == product_id) and (
                    cell.capacity - cell.quantity) >= quantity:
                cell.add_items(target_product, quantity)
                placed = True
                break

        if not placed:
            raise ValueError("на складе нет подходящей ячейки или места")

        self.company_budget -= total_cost
        new_order = Order(self._next_order_id, "Закупка", product_id, quantity, total_cost)
        self.orders.append(new_order)
        self._next_order_id += 1

    def move_products(self, warehouse_id: int, pos_id: int, product_id: int, quantity: int) -> None:
        """Перемещает товар со склада в магазин

        Args:
            warehouse_id (int): откуда везем
            pos_id (int): куда везем
            product_id (int): что везем
            quantity (int): сколько везем

        Raises:
            ValueError: если обьекты не найдены или товара нет
        """

        target_warehouse = None

        for wh in self.warehouses:
            if wh.facility_id == warehouse_id:
                target_warehouse = wh
                break

        target_pos = None

        for pos in self.points_of_sale:
            if pos.facility_id == pos_id:
                target_pos = pos
                break

        if not target_warehouse or not target_pos:
            raise ValueError("не нашли склад или точку продаж")

        removed = False

        for cell in target_warehouse.cells:
            if cell.product and cell.product.product_id == product_id and cell.quantity >= quantity:
                cell.remove_items(quantity)
                removed = True
                break

        if not removed:
            raise ValueError("на складе нет столько этого товара")

        target_pos.receive_products(product_id, quantity)
        new_order = Order(self._next_order_id, "Перемещение", product_id, quantity, 0.0)
        self.orders.append(new_order)
        self._next_order_id += 1

    def process_sale(self, pos_id: int, customer_id: int, product_id: int, quantity: int) -> None:
        """Продает товар покупателю из магазина

        Args:
            pos_id (int): айди магазина где идет продажа
            customer_id (int): айди покупателя
            product_id (int): что продаем
            quantity (int): сколько штук

        Raises:
            ValueError: если что то пошло не так при поиске
        """

        target_pos = None

        for pos in self.points_of_sale:
            if pos.facility_id == pos_id:
                target_pos = pos
                break

        target_customer = None

        for cust in self.customers:
            if cust.person_id == customer_id:
                target_customer = cust
                break

        target_product = None

        for prod in self.product_catalog:
            if prod.product_id == product_id:
                target_product = prod
                break

        if not target_pos or not target_customer or not target_product:
            raise ValueError("не нашли магазин покупателя или товар")

        target_pos.sell_product(product_id, quantity, target_product.retail_price)
        sale_amount = quantity * target_product.retail_price
        target_customer.add_purchase_amount(sale_amount)
        self.company_budget += sale_amount

        new_order = Order(self._next_order_id, "Продажа", product_id, quantity, sale_amount, customer_id)
        self.orders.append(new_order)
        self._next_order_id += 1

    def get_company_profitability(self) -> str:
        """Считает сколько у нас сейчас денег и информацию по бюджету

        Returns:
            str: текст с текущим балансом
        """

        info = f"Текущий бюджет компании: {self.company_budget} руб"

        return info
