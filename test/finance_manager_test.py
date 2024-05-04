import unittest
from unittest.mock import patch, mock_open
from finance_manager import FinanceManager
from finance_record import FinanceRecord


class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        self.finance_manager = FinanceManager()

    @patch('builtins.open', new_callable=mock_open,
           read_data="2022-01-01,доход,1000,Salary\n2022-01-02,расход,500,Groceries")
    def test_read_records_success(self, mock_file):
        success, records = self.finance_manager.read_records()
        self.assertTrue(success)
        self.assertEqual(len(records), 2)
        self.assertIsInstance(records[0], FinanceRecord)

    @patch('builtins.open', new_callable=mock_open, read_data="")
    def test_read_records_empty_file(self, mock_file):
        success, records = self.finance_manager.read_records()
        self.assertTrue(success)
        self.assertEqual(len(records), 0)

    @patch('builtins.open', side_effect=FileNotFoundError())
    def test_read_records_file_not_found(self, mock_file):
        success, records = self.finance_manager.read_records()
        self.assertFalse(success)
        self.assertEqual(len(records), 0)

    @patch('builtins.open', new_callable=mock_open,
           read_data="2022-01-01,доход,1000,Salary\n2022-01-02,расход,500,Groceries")
    def test_find_records_by_date(self, mock_file):
        success, records = self.finance_manager.find_records(date="2022-01-01")
        self.assertTrue(success)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].date, "2022-01-01")

    @patch('builtins.open', new_callable=mock_open,
           read_data="2022-01-01,доход,1000,Salary\n2022-01-02,расход,500,Groceries")
    def test_find_records_by_type(self, mock_file):
        success, records = self.finance_manager.find_records(record_type="доход")
        self.assertTrue(success)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].record_type.value, "доход")

    @patch('builtins.open', new_callable=mock_open,
           read_data="2022-01-01,доход,1000,Salary\n2022-01-02,расход,500,Groceries")
    def test_find_records_by_amount(self, mock_file):
        success, records = self.finance_manager.find_records(amount=500)
        self.assertTrue(success)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].amount, 500)

    @patch('builtins.open', new_callable=mock_open,
           read_data="2022-01-01,доход,1000,Salary\n2022-01-02,расход,500,Groceries")
    def test_calculate_balance(self, mock_file):
        income, expense, balance = self.finance_manager.calculate_balance()
        self.assertEqual(income, 1000)
        self.assertEqual(expense, 500)
        self.assertEqual(balance, 500)

    @patch('builtins.open', new_callable=mock_open,
           read_data="2022-01-01,доход,1000,Salary\n2022-01-02,расход,500,Groceries")
    def test_edit_record_success(self, mock_file):
        success, message = self.finance_manager.edit_record("2022-01-01", new_amount=2000)
        self.assertTrue(success)
        self.assertEqual(message, "Record successfully updated.")

    @patch('builtins.open', new_callable=mock_open,
           read_data="2022-01-01,доход,1000,Salary\n2022-01-02,расход,500,Groceries")
    def test_edit_record_not_found(self, mock_file):
        success, message = self.finance_manager.edit_record("2022-01-03", new_amount=2000)
        self.assertFalse(success)
        self.assertEqual(message, "Record for update not found.")


if __name__ == '__main__':
    unittest.main()
