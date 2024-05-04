class FinanceRecord:
    """
    A class used to represent a Finance Record.

    """

    def __init__(self, date, record_type, amount, description):
        """
        Constructs all the necessary attributes for the finance record object.

        Parameters
        ----------
            date : str
                The date of the finance record
            record_type : str
                The type of the finance record (e.g., 'income', 'expense')
            amount : int
                The amount of money involved in the finance record
            description : str
                A brief description of the finance record
        """
        self.date = date
        """
        The date attribute is a string representing the date of the finance record.
        """
        self.record_type = record_type
        """
        The record_type attribute is a string representing the type of the finance record.
        """
        self.amount = int(amount)
        """
        The amount attribute is an integer representing the amount of money involved in the finance record.
        """
        self.description = description
        """
        The description attribute is a string representing a brief description of the finance record.
        """

    def __str__(self):
        """
        Returns a string representation of the finance record.

        Returns
        -------
        str
            A string representation of the finance record.
        """
        return f"{self.date}, {self.record_type}, {self.amount}, {self.description}"

    def to_list(self):
        """
        Returns a list representation of the finance record for CSV.

        Returns
        -------
        list
            A list representation of the finance record for CSV.
        """
        return [self.date, self.record_type, self.amount, self.description]