import unittest
from unittest.mock import MagicMock

from finance_app import FinanceApp
from finance_manager import FinanceManager
from finance_record import FinanceRecord


class TestFinanceApp(unittest.TestCase):
    def setUp(self):
        self.app = FinanceApp()

    def test_add_record_ui_success(self):
        record = FinanceRecord('2022-01-01', 'доход', 1000, 'Salary')
        self.app.manager.add_record = MagicMock(return_value=True)
        self.app.add_record_ui = MagicMock(return_value=record)
        self.assertEqual(self.app.add_record_ui(), record)

    def test_edit_record_ui_success(self):
        record = FinanceRecord('2022-01-01', 'доход', 1000, 'Salary')
        self.app.manager.edit_record = MagicMock(return_value=(True, "Record successfully updated."))
        self.app.edit_record_ui = MagicMock(return_value=record)
        self.assertEqual(self.app.edit_record_ui(), record)

    def test_search_records_ui_success(self):
        record = FinanceRecord('2022-01-01', 'доход', 1000, 'Salary')
        self.app.manager.find_records = MagicMock(return_value=(True, [record]))
        self.app.search_records_ui = MagicMock(return_value=record)
        self.assertEqual(self.app.search_records_ui(), record)

    def test_display_balance_ui_success(self):
        self.app.manager.calculate_balance = MagicMock(return_value=(1000, 500, 500))
        self.app.display_balance_ui = MagicMock(return_value=(1000, 500, 500))
        self.assertEqual(self.app.display_balance_ui(), (1000, 500, 500))

    def test_main_loop_quit(self):
        self.app.main_loop = MagicMock(return_value=None)
        self.assertEqual(self.app.main_loop(), None)


if __name__ == '__main__':
    unittest.main()
