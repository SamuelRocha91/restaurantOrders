# 🍝🦐 Chapa Quente 🍛🥘 - Генератор Меню

<h2>🌐</h2>
<ul>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders" target="_blank">Português</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_es.md" target="_blank">Español</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_en.md" target="_blank">English</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ru.md" target="_blank">Русский</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ch.md" target="_blank">中文</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ar.md" target="_blank">العربية</a></li>
</ul>

![Работа с классами в Python REPL](./gifs/pythonRestaurant.gif)

Этот проект был разработан для ресторана **Chapa Quente** с целью создания эффективного инструмента для создания меню с учетом диетических ограничений клиентов и доступности ингредиентов на складе. В настоящее время управление рецептами и запасами осуществляется неэффективно с помощью файлов CSV, и этот проект нацелен на решение этой проблемы с более организованным и функциональным подходом.

## 🛠️ Реализованные функции

- **Картирование блюд и рецептов**: Была создана класс для картирования блюд и их соответствующих ингредиентов и количеств.
- **Генератор меню**: Реализован класс, отвечающий за генерацию меню на основе диетических ограничений и доступности ингредиентов.
- **Управление запасами**: Реализован класс для управления запасами ингредиентов, обеспечивающий возможность приготовления доступных блюд с имеющимися ингредиентами на складе.
- **Тестирование**: Реализованы тесты с использованием фреймворка `pytest`, покрывающие функциональность приложения, такие как валидация блюд, ингредиентов и ограничений.

## 🚵 Практические навыки

- **Использование Hashmaps с Dict и Set**: Использование структур `dict` и `set` Python для управления блюдами и ингредиентами.
- **Тестирование программного обеспечения**: Практика написания модульных тестов для классов с использованием `pytest`.
- **Объектно-ориентированное программирование**: Реализация классов, методов и атрибутов, следующих принципам объектно-ориентированного программирования.

## 📋 Требования

- Python 3.8 или выше
- Pip (менеджер пакетов Python)

## 🔧 Установка и запуск

Следуйте инструкциям ниже, чтобы клонировать и запустить проект на вашем локальном компьютере:

### 1. Клонируйте репозиторий

```bash
git clone git@github.com:SamuelRocha91/restaurantOrders.git
```

### 2. Перейдите в каталог проекта

```bash
cd restaurantOrders
```

### 3. Создайте виртуальную среду (опционально, но рекомендуется)

```bash
python3 -m venv venv
source venv/bin/activate  # В Windows используйте: venv\Scripts\activate
```

### 4. Установите зависимости

Установите зависимости, указанные в файлах `requirements.txt` и `dev-requirements.txt`:

```bash
pip install -r dev-requirements.txt
```

### 5. Запустите тесты

Чтобы запустить автоматические тесты, используйте команду:

```bash
pytest --cov=src --cov-report=term-missing
```

## 📝 Структура файлов

Структура проекта организована следующим образом:

```
.
├── src/
│   ├── models/
│   │   ├── dish.py            # Реализация класса Dish
│   │   ├── ingredient.py      # Реализация класса Ingredient
│   │   └── stock.py           # Реализация класса Stock (Управление запасами)
├── tests/
│   ├── test_dish.py           # Тесты для класса Dish
│   ├── test_ingredient.py     # Тесты для класса Ingredient
│   └── test_stock.py          # Тесты для класса Stock
├── dev-requirements.txt       # Зависимости для разработки и тестирования
├── requirements.txt           # Основные зависимости проекта
└── README.md                  # Документация проекта
```

## 📦 Зависимости

Зависимости проекта включают:

- [black](https://github.com/psf/black): Форматирование кода.
- [faker](https://github.com/joke2k/faker): Генерация фальшивых данных для тестирования.
- [flake8](https://github.com/PyCQA/flake8): Инструмент для линтинга.
- [httpx](https://www.python-httpx.org/): Библиотека HTTP-запросов.
- [pytest](https://pytest.org/): Фреймворк для тестирования.
- [pytest-cov](https://github.com/pytest-dev/pytest-cov): Отчеты о покрытии тестов.
- [pytest-json](https://github.com/nicoddemus/pytest-json): Плагин для вывода тестов в формате JSON.
- [pytest-unordered](https://github.com/altendky/pytest-unordered): Плагин для проверки неупорядоченного равенства множеств.
