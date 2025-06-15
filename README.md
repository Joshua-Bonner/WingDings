# WingDings Shop (Sample Project)

This is a sample Python project for a fictional shop that sells "wingdings."  
The purpose of this project is to practice using various Python libraries and tools, including:

- **Pydantic** for data validation and modeling
- **pytest** for unit testing
- **pipenv** for dependency management
- **black** for code formatting
- **flake8** for linting
- **Git** for version control
- And more!

## Project Structure

```
WingDings/
├── src/
│   ├── helpers/
│   ├── models/
├── tests/
├── Pipfile
├── Pipfile.lock
├── README.md
├── setup.cfg
├── pyproject.toml
```

## Features

- Manage a catalog of wingdings with properties like UUID, name, serial number, type, supplier, count, price, and stock status.
- Read and write wingding data in JSON format.
- Unit tests for core functionality.
- Example usage of modern Python best practices.

## Getting Started

1. **Clone the repository:**
   ```
   git clone https://github.com/Joshua-Bonner/WingDings.git
   cd WingDings
   ```

2. **Install dependencies:**
   ```
   pipenv install --dev
   ```

3. **Activate the virtual environment:**
   ```
   pipenv shell
   ```

4. **Run the application:**
   You can run the main application script or any specific module you want to test. For example:
   ```
   python src/main.py
   ```

6. **Run tests:**
   ```
   pipenv run pytest -p no:cacheprovider
   ```

5. **Format code with Black:**
   ```
   pipenv run black .
   ```

6. **Lint code:**
   ```
   pipenv run flake8 .
   ```

7. **Explore the code and try out your own features!**

## Why Wingdings?

This project is for learning and experimentation.  
"Shop for wingdings" is just a fun, fictional scenario to practice Python development.

---

Feel free to fork, modify, and use this project as a playground for Python libraries and tooling!