import json
import os
from CRMsystem import CrmSystem
from Employee import Employee
from Customer import Customer
from Product import Product


class DataManager:
    """Класс для сохранения и загрузки базы данных в формате JSON"""

    @staticmethod
    def save_data(system: CrmSystem, filename: str = "crm_data.json") -> None:
        """Разбираем нашу систему на словари и сохраняем в JSON

        Args:
            system (CrmSystem): главная система
            filename (str, optional): имя файла

        Raises:
            TypeError: если передали не систему
        """

        if not isinstance(system, CrmSystem):
            raise TypeError("сохранять можно только обьект CrmSystem")

        data_to_save = {
            "budget": system.company_budget,
            "next_order_id": system._next_order_id,
            "employees": [],
            "customers": [],
            "catalog": []
        }

        for emp in system.employees:
            emp_dict = {
                "person_id": getattr(emp, "person_id", getattr(emp, "_person_id", None)),
                "name": emp.name,
                "phone": emp.phone,
                "position": emp.position,
                "salary": emp.salary,
                "facility_id": emp.assigned_facility_id
            }
            data_to_save["employees"].append(emp_dict)

        for cust in system.customers:
            cust_dict = {
                "person_id": getattr(cust, "person_id", getattr(cust, "_person_id", None)),
                "name": cust.name,
                "phone": cust.phone,
                "total_spent": cust.total_spent
            }
            data_to_save["customers"].append(cust_dict)

        for prod in system.product_catalog:
            prod_dict = {
                "product_id": prod.product_id,
                "name": prod.name,
                "purchase_price": prod.purchase_price,
                "retail_price": prod.retail_price
            }
            data_to_save["catalog"].append(prod_dict)

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data_to_save, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_data(filename: str = "crm_data.json") -> CrmSystem:
        """Загружает данные из JSON и собирает из них классы

        Args:
            filename (str, optional): откуда грузим

        Returns:
            CrmSystem: готовая система
        """

        system = CrmSystem()

        if not os.path.exists(filename):
            return system

        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        system.company_budget = data.get("budget", 100000.0)
        system._next_order_id = data.get("next_order_id", 1)

        for emp_data in data.get("employees", []):
            new_emp = Employee(
                emp_data["person_id"],
                emp_data["name"],
                emp_data["phone"],
                emp_data["position"],
                emp_data["salary"],
                emp_data["facility_id"]
            )
            system.employees.append(new_emp)

        for cust_data in data.get("customers", []):
            new_cust = Customer(
                cust_data["person_id"],
                cust_data["name"],
                cust_data["phone"],
                cust_data["total_spent"]
            )
            system.customers.append(new_cust)

        for prod_data in data.get("catalog", []):
            new_prod = Product(
                prod_data["product_id"],
                prod_data["name"],
                prod_data["purchase_price"],
                prod_data["retail_price"]
            )
            system.product_catalog.append(new_prod)

        return system
