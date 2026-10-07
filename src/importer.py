import csv
from datetime import datetime
from decimal import Decimal
from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Transaction


def clean_text(text):
    return " ".join(text.split())


def load_transactions(file_path):
    transactions = []

    # Chase CSV:
    # Details, Posting Date, Description, Amount, Type, Balance, Check or Slip
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row_lst in reader:
            posting_date = datetime.strptime(
                row_lst[1], "%m/%d/%Y"
            ).date()

            transaction = Transaction(
                transaction_type=clean_text(row_lst[0]),
                posting_date=posting_date,
                description=clean_text(row_lst[2]),
                amount=Decimal(row_lst[3]),
                balance=Decimal(row_lst[5]),
                category="Uncategorized"
            )

            transactions.append(transaction)

    return transactions

def save_transactions(db: Session, transactions):
    added = 0
    skipped = 0

    for transaction in transactions:
        statement = select(Transaction).where(
            Transaction.posting_date == transaction.posting_date,
            Transaction.description == transaction.description,
            Transaction.amount == transaction.amount,
            Transaction.transaction_type == transaction.transaction_type
        )

        existing_transaction = db.scalar(statement)

        if existing_transaction is None:
            db.add(transaction)
            added += 1
        else:
            skipped += 1

    db.commit()

    return added, skipped