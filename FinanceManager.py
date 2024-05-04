import csv

from FinanceRecord import FinanceRecord


class FinanceManager:
    """
    A class used to manage finance records.

    """

    def __init__(self, filename='finance_records.csv'):
        """
        Constructs all the necessary attributes for the finance manager object.

        Parameters
        ----------
            filename : str
                The name of the file where the finance records are stored
        """
        self.filename = filename
        """
        The filename attribute is a string representing the name of the file where the finance records are stored.
        """
    def read_records(self):
        """
        Reads the finance records from the file.

        Returns
        -------
        tuple
            A tuple containing a boolean indicating the success of the operation and a list of records.
        """
        records = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        record = FinanceRecord(*row)
                        records.append(record)
            return True, records
        except FileNotFoundError:
            print("File not found.")
            return False, []
        except Exception as e:
            print(f"ERROR: {e}")
            return False, []

    def find_records(self, date=None, record_type=None, amount=None):
        """
        Finds records that match the given criteria.

        Parameters
        ----------
            date : str
                The date of the finance record
            record_type : str
                The type of the finance record (e.g., 'income', 'expense')
            amount : int
                The amount of money involved in the finance record

        Returns
        -------
        tuple
            A tuple containing a boolean indicating the success of the operation and a list of records.
        """
        success, records = self.read_records()
        if not success:
            return False, []
        try:
            if date:
                records = [record for record in records if record.date == date]
            if record_type:
                records = [record for record in records if record.record_type == record_type]
            if amount is not None:
                amount = int(amount)
                records = [record for record in records if record.amount == amount]
            return True, records
        except ValueError:
            print("ERROR: Uncorrected value.")
            return False, []
        except Exception as e:
            print(f"ERROR: {e}")
            return False, []

    def add_record(self, record):
        """
        Adds a new record to the file.

        Parameters
        ----------
            record : FinanceRecord
                The record to be added

        Returns
        -------
        bool
            A boolean indicating the success of the operation.
        """
        try:
            with open(self.filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([record.date, record.record_type, record.amount, record.description])
            return True  # Successfully added
        except Exception as e:
            print(f"Error when adding record: {e}")
            return False  # Error when adding

    def update_records(self, records):
        """
        Updates the records in the file.

        Parameters
        ----------
            records : list
                The list of records to be updated

        Returns
        -------
        bool
            A boolean indicating the success of the operation.
        """
        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(
                    [record.to_list() for record in records])
            return True
        except Exception as e:
            print(f"Error when updating file: {e}")
            return False

    def calculate_balance(self):
        """
        Calculates the total income, expense and balance.

        Returns
        -------
        tuple
            A tuple containing the total income, expense and balance.
        """
        success, records = self.read_records()
        if not success:
            return 0, 0, 0
        try:
            income = sum(record.amount for record in records if record.record_type.lower() == 'доход')
            expense = sum(record.amount for record in records if record.record_type.lower() == 'расход')
            return income, expense, income - expense
        except Exception as e:
            print(f"Error when calculating balance: {e}")
            return 0, 0, 0

    def edit_record(self, date, new_type=None, new_amount=None, new_description=None):
        """
        Edits a record that matches the given date.

        Parameters
        ----------
            date : str
                The date of the finance record
            new_type : str
                The new type of the finance record (e.g., 'income', 'expense')
            new_amount : int
                The new amount of money involved in the finance record
            new_description : str
                The new description of the finance record

        Returns
        -------
        tuple
            A tuple containing a boolean indicating the success of the operation and a message.
        """
        success, records = self.read_records()
        if not success:
            return False, "Error reading file."

        updated = False
        for record in records:
            if record.date == date:
                if new_type:
                    record.record_type = new_type
                if new_amount is not None:
                    try:
                        record.amount = int(new_amount)
                    except ValueError:
                        return False, "Incorrect value for amount."
                if new_description:
                    record.description = new_description
                updated = True
                break
        if not updated:
            return False, "Record for update not found."

        if self.update_records(records):
            return True, "Record successfully updated."
        else:
            return False, "Error when updating file."

