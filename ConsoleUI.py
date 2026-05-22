from CRMsystem import CrmSystem
from Employee import Employee
from Customer import Customer
from Product import Product


class ConsoleUI:
    """Класс для работы с пользователем через консоль"""

    def __init__(self, crm_system: CrmSystem) -> None:
        """Инициализация меню

        Args:
            crm_system (CrmSystem): главная система к которой будем обращаться

        Raises:
            TypeError: если передали кривую систему
        """

        if not isinstance(crm_system, CrmSystem):
            raise TypeError("интерфейсу нужна нормальная CrmSystem")

        self.crm = crm_system

    def start(self) -> None:
        """Главный цикл программы"""

        while True:
            print("\n=== Главное меню CRM ===")
            print("1 - Нанять работника")
            print("2 - Зарегистрировать клиента")
            print("3 - Добавить товар в каталог")
            print("4 - Посмотреть бюджет компании")
            print("5 - Выйти и сохранить")

            choice = input("Выберите действие: ")
            
            if choice == "1":
                self._ui_hire_employee()

            elif choice == "2":
                self._ui_add_customer()

            elif choice == "3":
                self._ui_add_product()

            elif choice == "4":
                print(self.crm.get_company_profitability())

            elif choice == "5":
                break

            else:
                print("нет такого пункта попробуй еще раз")

    def _ui_hire_employee(self) -> None:
        """Метод для ввода данных нового работника с клавиатуры"""

        try:
            emp_id = int(input("Введите айдишник работника: "))
            name = input("Введите имя: ")
            phone = input("Введите телефон: ")
            position = input("Должность: ")
            salary = float(input("Зарплата: "))

            new_emp = Employee(emp_id, name, phone, position, salary)
            self.crm.hire_employee(new_emp)
            print("работник успешно добавлен в базу")

        except ValueError as e:
            print(f"вы ввели что то не то: {e}")

        except TypeError as e:
            print(f"ошибка типов: {e}")

    def _ui_add_customer(self) -> None:
        """Метод чтобы создать клиента"""

        try:
            cust_id = int(input("Введите айди клиента: "))
            name = input("Введите имя клиента: ")
            phone = input("Введите телефон: ")

            new_cust = Customer(cust_id, name, phone)
            self.crm.customers.append(new_cust)
            print("клиент успешно записан")

        except ValueError as e:
            print(f"ошибка при вводе данных: {e}")

    def _ui_add_product(self) -> None:
        """Метод для пополнения каталога товаров"""

        try:
            prod_id = int(input("Введите айди товара: "))
            name = input("Название товара: ")
            purch_price = float(input("Почем закупаем: "))
            retail_price = float(input("Почем продаем: "))

            new_prod = Product(prod_id, name, purch_price, retail_price)
            self.crm.add_product_to_catalog(new_prod)
            print("товар добавлен в каталог можно закупать")

        except ValueError as e:
            print(f"косяк с данными: {e}")
