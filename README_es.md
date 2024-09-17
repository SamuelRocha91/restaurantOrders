# 🍝🦐 Chapa Quente 🍛🥘 - Generador de Menús

<h2>🌐</h2>
<ul>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders" target="_blank">Português</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_es.md" target="_blank">Español</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_en.md" target="_blank">English</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ru.md" target="_blank">Русский</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ch.md" target="_blank">中文</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ar.md" target="_blank">العربية</a></li>
</ul>

![Manipulación de clases en el REPL de Python](./gifs/pythonRestaurant.gif)

Este proyecto fue desarrollado para el restaurante **Chapa Quente** con el objetivo de crear una herramienta eficiente para la construcción de menús, considerando las restricciones alimentarias de los clientes y la disponibilidad de ingredientes en el inventario. Actualmente, la gestión de recetas e inventario se realiza de manera ineficiente mediante archivos CSV, y este proyecto tiene como objetivo resolver ese problema con un enfoque más organizado y funcional.

## 🛠️ Funcionalidades Implementadas

- **Mapeo de platos y recetas**: Se creó una clase que mapea los platos con sus respectivos ingredientes y cantidades.
- **Generador de menús**: Implementación de una clase responsable de generar menús basados en restricciones alimentarias y disponibilidad de ingredientes.
- **Gestión de inventario**: Clase implementada para gestionar el inventario de ingredientes, asegurando que los platos disponibles puedan ser preparados con los ingredientes en stock.
- **Pruebas**: Implementación de pruebas utilizando el framework `pytest`, cubriendo las funcionalidades de la aplicación, como la validación de platos, ingredientes y restricciones.

## 🚵 Habilidades Practicadas

- **Uso de Hashmaps con Dict y Set**: Uso de las estructuras `dict` y `set` de Python para gestionar platos e ingredientes.
- **Pruebas de software**: Práctica de escritura de pruebas unitarias para clases usando `pytest`.
- **Programación Orientada a Objetos**: Implementación de clases, métodos y atributos que siguen los principios de la programación orientada a objetos.

## 📋 Requisitos

- Python 3.8 o superior
- Pip (gestor de paquetes de Python)

## 🔧 Instalación y Ejecución

Sigue las instrucciones a continuación para clonar y ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```

### 2. Navegar al directorio del proyecto

```bash
cd tu-repositorio
```

### 3. Crear un entorno virtual (opcional, pero recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows, usa: venv\Scripts\activate
```

### 4. Instalar las dependencias

Instala las dependencias descritas en el archivo `requirements.txt` y en el archivo `dev-requirements.txt`:

```bash
pip install -r dev-requirements.txt
```

### 5. Ejecutar las pruebas

Para ejecutar las pruebas automatizadas, utiliza el siguiente comando:

```bash
pytest --cov=src --cov-report=term-missing
```

## 📝 Estructura de Archivos

La estructura del proyecto está organizada de la siguiente manera:

```
.
├── src/
│   ├── models/
│   │   ├── dish.py            # Implementación de la clase Dish
│   │   ├── ingredient.py      # Implementación de la clase Ingredient
│   │   └── stock.py           # Implementación de la clase Stock (Gestión de Inventario)
├── tests/
│   ├── test_dish.py           # Pruebas para la clase Dish
│   ├── test_ingredient.py     # Pruebas para la clase Ingredient
│   └── test_stock.py          # Pruebas para la clase Stock
├── dev-requirements.txt       # Dependencias para el desarrollo y pruebas
├── requirements.txt           # Dependencias principales del proyecto
└── README.md                  # Documentación del proyecto
```

## 📦 Dependencias

Las dependencias del proyecto incluyen:

- [black](https://github.com/psf/black): Formateador de código.
- [faker](https://github.com/joke2k/faker): Generación de datos falsos para pruebas.
- [flake8](https://github.com/PyCQA/flake8): Herramienta de linting.
- [httpx](https://www.python-httpx.org/): Biblioteca para solicitudes HTTP.
- [pytest](https://pytest.org/): Framework de pruebas.
- [pytest-cov](https://github.com/pytest-dev/pytest-cov): Informes de cobertura de pruebas.
- [pytest-json](https://github.com/nicoddemus/pytest-json): Plugin para la salida JSON de las pruebas.
- [pytest-unordered](https://github.com/altendky/pytest-unordered): Plugin para verificar la igualdad de conjuntos de manera no ordenada.
