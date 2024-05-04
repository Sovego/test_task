import unittest

from finance_record import FinanceRecord


class FinanceRecordTests(unittest.TestCase):

    def setUp(self):
        self.record = FinanceRecord("2022-01-01", "доход", 1000, "Salary")

    def record_to_string(self):
        self.assertEqual(str(self.record), "2022-01-01, доход, 1000, Salary")

    def record_to_list(self):
        self.assertEqual(self.record.to_list(), ["2022-01-01", "доход", 1000, "Salary"])

    def record_attributes(self):
        self.assertEqual(self.record.date, "2022-01-01")
        self.assertEqual(self.record.record_type, "доход")
        self.assertEqual(self.record.amount, 1000)
        self.assertEqual(self.record.description, "Salary")


if __name__ == '__main__':
    unittest.main()
