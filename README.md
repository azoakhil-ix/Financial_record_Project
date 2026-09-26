## 📦 Installation & Setup

Follow these steps to get your development environment configured. While this project currently uses Python's built-in libraries, these steps ensure your environment stays clean and organized as the project grows.

### 1. Clone the Repository
Open your terminal and clone the project to your local machine:
```bash
git clone https://github.com
cd transaction-analyzer
```

### 2. Prepare Your Chase Data (Required)
This project requires a transaction history file from your Chase checking account to run.

1. Log into your **Chase Online Banking** account.
2. Export or download your recent checking account activity as a **CSV** file.
3. **Rename the file:** Chase automatically names this file using your account details (e.g., `Chase2552_Activity_20260919.csv`). To protect your privacy and ensure the script recognizes it, rename the file to **`chase_activity.csv`**.
4. Place the renamed file directly into the root directory of this project.

> 🔒 **Security Note:** Never commit your real financial data to GitHub. Ensure `chase_activity.csv` is added to your `.gitignore` file before pushing any code.

### 3. Set Up a Virtual Environment (Recommended)
Isolate your project dependencies by creating a local virtual environment:

* **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 4. Install Dependencies
When the project expands to use external tools (like `pandas` for advanced data tracking or `matplotlib` for generating financial charts), install them instantly using the package manager:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> 💡 **Note for Contributors:** If you install any new external libraries during development, remember to freeze your environment changes back into the text file by running: `pip freeze > requirements.txt`.
