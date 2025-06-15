# WingDings Shop (Sample Project)

This is a sample Python project for a fictional shop that sells "wingdings."  
The purpose of this project is to practice using various Python libraries and tools, including:

- **Pydantic** for data validation and modeling
- **pytest** for unit testing
- **pipenv** for dependency management
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
```

## Features

- Manage a catalog of wingdings with properties like UUID, name, serial number, type, supplier, count, price, and stock status.
- Read and write wingding data in JSON format.
- Unit tests for core functionality.
- Example usage of modern Python best practices.

## Getting Started

1. **Clone the repository:**
   ```
   git clone <your-repo-url>
   cd WingDings
   ```

2. **Install dependencies:**
   ```
   pipenv install --dev
   ```

3. **Run tests:**
   ```
   pipenv run pytest -p no:cacheprovider
   ```

4. **Explore the code and try out your own features!**

## Why Wingdings?

This project is for learning and experimentation.  
"Shop for wingdings" is just a fun, fictional scenario to practice Python development.

---

Feel free to fork, modify, and use this project as a playground for Python libraries and tooling!