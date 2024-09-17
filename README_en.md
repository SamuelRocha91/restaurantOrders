# 🍝🦐 Chapa Quente 🍛🥘 - Menu Generator

<h2>🌐</h2>
<ul>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders" target="_blank">Português</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_es.md" target="_blank">Español</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_en.md" target="_blank">English</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ru.md" target="_blank">Русский</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ch.md" target="_blank">中文</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ar.md" target="_blank">العربية</a></li>
</ul>

![Class handling in Python REPL](./gifs/pythonRestaurant.gif)

This project was developed for the **Chapa Quente** restaurant with the goal of creating an efficient tool for building menus, considering customer dietary restrictions and ingredient availability in the inventory. Currently, recipe and inventory management is done inefficiently through CSV files, and this project aims to solve this problem with a more organized and functional approach.

## 🛠️ Implemented Features

- **Dish and recipe mapping**: A class was created that maps dishes to their respective ingredients and quantities.
- **Menu generator**: A class responsible for generating menus based on dietary restrictions and ingredient availability was implemented.
- **Inventory management**: A class was implemented to manage the stock of ingredients, ensuring that available dishes can be prepared with the ingredients in stock.
- **Testing**: Implementation of tests using the `pytest` framework, covering application functionalities such as dish validation, ingredients, and restrictions.

## 🚵 Skills Practiced

- **Using Hashmaps with Dict and Set**: Usage of Python's `dict` and `set` structures to manage dishes and ingredients.
- **Software testing**: Practice of writing unit tests for classes using `pytest`.
- **Object-Oriented Programming**: Implementation of classes, methods, and attributes that follow object-oriented principles.

## 📋 Requirements

- Python 3.8 or higher
- Pip (Python's package manager)

## 🔧 Installation and Execution

Follow the instructions below to clone and run the project on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the project directory

```bash
cd your-repository
```

### 3. Create a virtual environment (optional, but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 4. Install dependencies

Install the dependencies listed in the `requirements.txt` and `dev-requirements.txt` files:

```bash
pip install -r dev-requirements.txt
```

### 5. Run the tests

To run the automated tests, use the following command:

```bash
pytest --cov=src --cov-report=term-missing
```

## 📝 File Structure

The project structure is organized as follows:

```
.
├── src/
│   ├── models/
│   │   ├── dish.py            # Implementation of the Dish class
│   │   ├── ingredient.py      # Implementation of the Ingredient class
│   │   └── stock.py           # Implementation of the Stock class (Inventory Management)
├── tests/
│   ├── test_dish.py           # Tests for the Dish class
│   ├── test_ingredient.py     # Tests for the Ingredient class
│   └── test_stock.py          # Tests for the Stock class
├── dev-requirements.txt       # Dependencies for development and testing
├── requirements.txt           # Main project dependencies
└── README.md                  # Project documentation
```

## 📦 Dependencies

Project dependencies include:

- [black](https://github.com/psf/black): Code formatter.
- [faker](https://github.com/joke2k/faker): Fake data generation for testing.
- [flake8](https://github.com/PyCQA/flake8): Linting tool.
- [httpx](https://www.python-httpx.org/): HTTP requests library.
- [pytest](https://pytest.org/): Testing framework.
- [pytest-cov](https://github.com/pytest-dev/pytest-cov): Test coverage reports.
- [pytest-json](https://github.com/nicoddemus/pytest-json): Plugin for JSON test output.
- [pytest-unordered](https://github.com/altendky/pytest-unordered): Plugin to verify unordered set equality.
