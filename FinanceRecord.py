class FinanceRecord:
    """
    A class used to represent a Finance Record.

    ...

    Attributes
    ----------
    date : str
        The date of the finance record
    record_type : str
        The type of the finance record (e.g., 'income', 'expense')
    amount : int
        The amount of money involved in the finance record
    description : str
        A brief description of the finance record

    Methods
    -------
    __str__():
        Returns a string representation of the finance record.
    to_list():
        Returns a list representation of the finance record for CSV.
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
        self.record_type = record_type
        self.amount = int(amount)
        self.description = description

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