import csv
from datetime import *
from dateutil.relativedelta import relativedelta

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


def clean_text(text):
    return " ".join(text.split())

def load_transactions(file_path):
    transactions = []
    # Details,Posting Date,Description,Amount,Type,Balance,Check or Slip #
    # the following block of code reads the csv file and stores each transaction as objects in a list.
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        # today = date.today()# todays date
        for row_lst in reader:
            #row_lst is a list of strings, each string is a column in the csv file. some elements can be empty.
            curr_date = datetime.strptime(row_lst[1], "%m/%d/%Y").date() # convert string to date object
            transaction = Transaction((clean_text(row_lst[0])),curr_date, (clean_text(row_lst[2])), row_lst[3],row_lst[4],row_lst[5],row_lst[6])
            transactions.append(transaction)
    return transactions


file = "data/private/Bank_Activity_20260919.csv"
transactions = load_transactions(file)
    

revenue = 0
expense = 0
for tr in transactions:
    amt = abs(tr.amount)
    print(tr.type)
    if "CREDIT" in tr.details:
        revenue += int(amt*100)/100
    elif "DEBIT" in tr.details:
        expense += int(amt*100)/100
print(f"Revenue in the last month: {revenue}")
print(f"Expense in the last month: {expense}")

