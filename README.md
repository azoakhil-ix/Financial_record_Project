## 📦 Installation & Setup

Follow these steps to get your development environment configured. While this project currently uses Python's built-in libraries, these steps ensure your environment stays clean and organized as the project grows.

### 1. Clone the Repository
Open your terminal and clone the project to your local machine:
```bash
git clone https://github.com
cd transaction-analyzer
```

### 2. Set Up a Virtual Environment (Recommended)
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

### 3. Install Dependencies
When the project expands to use external tools (like `pandas` for advanced data tracking or `matplotlib` for generating financial charts), install them instantly using the package manager:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> 💡 **Note for Contributors:** If you install any new external libraries during development, remember to freeze your environment changes back into the text file by running: `pip freeze > requirements.txt`.