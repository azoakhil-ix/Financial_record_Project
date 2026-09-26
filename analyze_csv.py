import csv
# from datetime import date

class Transaction:
    # The constructor method (Equivalent to a Java Constructor)
    def __init__(self, details, date, description, amount, type, balance, check_or_slip):
        self.details = details
        self.date = date
        self.description = description
        self.amount = float(amount)
        self.type = type
        self.balance = balance
        self.check_or_slip = check_or_slip

# Details,Posting Date,Description,Amount,Type,Balance,Check or Slip #
file_name = "Chase2552_Activity_20260919.csv"
transactions = []
with open(file_name, "r",encoding="utf-8") as file:
    reader = csv.reader(file)
    starting_date = "2026-08-19"
    for row_lst in reader:
        date_raw = row_lst[1].split("/")
        date = f"{date_raw[2]}-{date_raw[0]}-{date_raw[1]}"
        if date < starting_date:
            break
        transaction = Transaction(row_lst[0],date, row_lst[2], row_lst[3],row_lst[4],row_lst[5],row_lst[6],row_lst[7])
        transactions.append(transaction)



    # Equivalent to Java's toString() method
    def __repr__(self):
        return f"Transaction({self.date}, {self.description}, ${self.amount:.2f})"
