from src.database import create_tables, SessionLocal
from src.importer import load_transactions, save_transactions
from src.models import Transaction

def main():
    create_tables()

    file_path = "data/private/Bank_Activity_20260919.csv"
    transactions = load_transactions(file_path)

    print(f"Loaded {len(transactions)} transactions from CSV.")

    db = SessionLocal()

    try:
        added, skipped = save_transactions(db, transactions)

        print(f"Added {added} new transactions.")
        print(f"Skipped {skipped} duplicate transactions.")
    finally:
        db.close()


if __name__ == "__main__":
    main()