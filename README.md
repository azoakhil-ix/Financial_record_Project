# Personal Expense & Decision System

A Python-based financial data system for importing, cleaning, storing, and analyzing transaction data.

The project currently uses **SQLAlchemy** and **SQLite** to transform raw bank transaction exports into structured, persistent transaction records. The import pipeline normalizes transaction data and detects previously imported transactions to prevent duplicate records.

## Current Features

- Import transaction data from CSV files
- Normalize transaction descriptions and transaction types
- Store transaction records persistently using SQLAlchemy ORM and SQLite
- Use decimal-based fields for monetary values
- Detect and skip previously imported transactions
- Keep private financial data outside version control

## In Development

- Automated transaction categorization
- Configurable categorization rules
- Spending and cash-flow analysis
- Machine-learning-assisted transaction classification
- Personal financial decision support

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/azoakhil-ix/Financial_record_Project
cd Financial_record_Project
```

### 2. Create a Virtual Environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Transaction Data

Create the private data directory:

```bash
mkdir -p data/private
```

Place your bank transaction CSV inside `data/private/`.

The current importer expects the Chase CSV format:

```text
Details, Posting Date, Description, Amount, Type, Balance, Check or Slip
```

Private transaction data and the local SQLite database are excluded from version control through `.gitignore`.

> **Security:** Never commit real bank transaction data, account information, `.env` files, or the generated financial database to a public repository.

## Running the Project

With the virtual environment activated:

```bash
python main.py
```

The application imports the transaction data, normalizes relevant fields, stores new transactions in SQLite, and skips transactions that have already been imported.

## Project Structure

```text
Financial_record_Project/
├── data/
│   └── private/          # Private transaction files (not committed)
├── src/
│   ├── database.py       # SQLite and SQLAlchemy configuration
│   ├── importer.py       # CSV parsing and transaction ingestion
│   └── models.py         # Database models
├── main.py               # Application entry point
├── requirements.txt
├── README.md
└── .gitignore
```

## Technology

- Python
- SQLAlchemy
- SQLite
- Git