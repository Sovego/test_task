from finance_manager import FinanceManager
from finance_record import FinanceRecord


class FinanceApp:
    """
    A class used to manage the user interface for the finance application.

    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the finance application object.
        """
        self.manager = FinanceManager()  # Create an instance of the FinanceManager class
        """
        The manager attribute is an instance of the FinanceManager class. It is used to manage finance records.
        """
    def __add_record_ui(self):
        """
        Handles the user interface for adding a new finance record.

        The user is prompted to input the date, type, amount, and description of the record.
        If the record is successfully added, a success message is printed.
        If the record is not successfully added, an error message is printed.
        """
        try:
            date = input("Введите дату (ГГГГ-ММ-ДД): ")
            record_type = input("Доход или расход? ").lower()
            amount = int(input("Введите сумму: "))
            description = input("Введите описание: ")
            record = FinanceRecord(date, record_type, amount, description)
            if self.manager.add_record(record):
                print("Запись успешно добавлена!")
            else:
                print("Не удалось добавить запись.")
        except ValueError:
            print("Ошибка: Некорректный ввод числа.")
        except Exception as e:
            print(f"Ошибка: {e}")

    def __edit_record_ui(self):
        """
        Handles the user interface for editing an existing finance record.

        The user is prompted to input the date of the record to be edited and the new values for the type, amount,
        and description. If the record is successfully edited, a success message is printed. If the record is not
        successfully edited, an error message is printed.
        """
        date = input("Введите дату записи для редактирования (ГГГГ-ММ-ДД): ")
        new_type = input("Введите новый тип (доход/расход, оставьте пустым, если не изменять): ").lower()
        new_amount = input("Введите новую сумму (оставьте пустым, если не изменять): ")
        new_description = input("Введите новое описание (оставьте пустым, если не изменять): ")

        if new_type == '':
            new_type = None
        if new_amount == '':
            new_amount = None
        if new_description == '':
            new_description = None

        success, message = self.manager.edit_record(date, new_type, new_amount, new_description)
        print(message)

    def __search_records_ui(self):
        """
        Handles the user interface for searching finance records.

        The user is prompted to select a search criterion (date, category, or amount) and input the corresponding value.
        The function then calls the find_records method of the manager with the selected criterion.
        If records are found, they are printed to the console.
        If no records are found, a message is printed to the console.
        If an error occurs during the search, an error message is printed to the console.
        """
        criteria = input("Выберите критерий поиска - дата (d), категория (c), сумма (s): ")
        try:
            if criteria == 'd':
                date = input("Введите дату (ГГГГ-ММ-ДД): ")
                success, found_records = self.manager.find_records(date=date)
            elif criteria == 'c':
                record_type = input("Введите категорию: ")
                success, found_records = self.manager.find_records(record_type=record_type)
            elif criteria == 's':
                amount = input("Введите сумму: ")
                success, found_records = self.manager.find_records(amount=amount)
            else:
                print("Неверный критерий поиска. Попробуйте снова.")
                return

            if not success:
                print("Произошла ошибка при поиске. Попробуйте снова.")
            elif found_records:
                print("Найденные записи:")
                for record in found_records:
                    print(f"Дата: {record.date}")
                    print(f"Категория: {record.record_type.value}")
                    print(f"Сумма: {record.amount}")
                    print(f"Описание: {record.description}\n")
            else:
                print("Записи не найдены.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def __display_balance_ui(self):
        """
        Handles the user interface for displaying the balance.

        The function calls the calculate_balance method of the manager and prints the income, expense, and balance to the
        console. If an error occurs during the calculation, an error message is printed to the console.
        """
        try:
            income, expense, balance = self.manager.calculate_balance()
            if income == 0 and expense == 0:
                print("В файле отсутствуют записи или файл пуст.")
            else:
                print(f"Общий доход: {income}, Общий расход: {expense}, Текущий баланс: {balance}")
        except Exception as e:
            print(f"Ошибка при выводе баланса: {e}")

    def main_loop(self):
        """
        Handles the main loop of the application.

        The user is prompted to select an action (display balance, add record, edit record, search, or quit).
        The selected action is then executed.
        If an error occurs during the execution of the action, an error message is printed to the console.
        """
        actions = {
            'b': self.__display_balance_ui,
            'a': self.__add_record_ui,
            'e': self.__edit_record_ui,
            's': self.__search_records_ui,
        }
        while True:
            action = input("Выберите действие: Вывод баланса (b), Добавление записи (a), Редактирование записи (e), "
                           "Поиск (s), Выход (q): ")
            if action == 'q':
                break
            action_method = actions.get(action)
            if action_method:
                try:
                    action_method()
                except Exception as e:
                    print(f"Ошибка выполнения: {e}")
            else:
                print("Неверный ввод, попробуйте снова.")
