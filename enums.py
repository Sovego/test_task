from enum import Enum


# Define an enumeration for the record types in the finance application.
# This Enum is used to avoid errors due to typos in string literals and make the code more readable and maintainable.
# The two record types are INCOME and EXPENSE, represented by the Russian words 'доход' and 'расход', respectively.
class RecordType(Enum):
    INCOME = 'доход'  # Represents an income record.
    EXPENSE = 'расход'  # Represents an expense record.
