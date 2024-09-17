# 🍝🦐 Chapa Quente 🍛🥘 - Gerador de Cardápios

<h2>🌐</h2>
<ul>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders" target="_blank">Português</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_es.md" target="_blank">Español</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_en.md" target="_blank">English</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ru.md" target="_blank">Русский</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ch.md" target="_blank">中文</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ar.md" target="_blank">العربية</a></li>
</ul>

![Manipulação de classes no REPL do Python](./gifs/pythonRestaurant.gif)

Este projeto foi desenvolvido para o restaurante **Chapa Quente** com o objetivo de criar uma ferramenta eficiente de construção de cardápios, considerando as restrições alimentares dos clientes e a disponibilidade de ingredientes no estoque. Atualmente, o gerenciamento de receitas e estoque é feito de maneira ineficiente através de arquivos CSV, e este projeto visa solucionar esse problema com uma abordagem mais organizada e funcional.

## 🛠️ Funcionalidades Implementadas

- **Mapeamento de pratos e receitas**: Foi criada uma classe que mapeia os pratos e seus respectivos ingredientes e quantidades.
- **Gerador de cardápios**: Implementação de uma classe responsável por gerar cardápios com base nas restrições alimentares e na disponibilidade de ingredientes.
- **Gestão de estoque**: Classe implementada para gerenciar o estoque de ingredientes, garantindo que os pratos disponíveis possam ser preparados com os ingredientes em estoque.
- **Testes**: Implementação de testes utilizando o framework `pytest`, cobrindo as funcionalidades da aplicação, como a validação de pratos, ingredientes e restrições.

## 🚵 Habilidades Exercitadas

- **Uso de Hashmaps com Dict e Set**: Utilização das estruturas `dict` e `set` do Python para gerenciamento de pratos e ingredientes.
- **Testes de software**: Prática de escrita de testes unitários para classes utilizando `pytest`.
- **Orientação a Objetos**: Implementação de classes, métodos e atributos que seguem os princípios de orientação a objetos.

## 📋 Requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

## 🔧 Instalação e Execução

Siga as instruções abaixo para clonar e executar o projeto em sua máquina local:

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Navegue até o diretório do projeto

```bash
cd seu-repositorio
```

### 3. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```

### 4. Instale as dependências

Instale as dependências descritas no arquivo `requirements.txt` e no arquivo `dev-requirements.txt`:

```bash
pip install -r dev-requirements.txt
```

### 5. Execute os testes

Para rodar os testes automatizados, utilize o comando:

```bash
pytest --cov=src --cov-report=term-missing
```

## 📝 Estrutura de Arquivos

A estrutura do projeto é organizada da seguinte forma:

```
.
├── src/
│   ├── models/
│   │   ├── dish.py            # Implementação da classe Dish
│   │   ├── ingredient.py      # Implementação da classe Ingredient
│   │   └── stock.py           # Implementação da classe Stock (Gestão de Estoque)
├── tests/
│   ├── test_dish.py           # Testes para a classe Dish
│   ├── test_ingredient.py     # Testes para a classe Ingredient
│   └── test_stock.py          # Testes para a classe Stock
├── dev-requirements.txt       # Dependências para o desenvolvimento e testes
├── requirements.txt           # Dependências principais do projeto
└── README.md                  # Documentação do projeto
```

## 📦 Dependências

As dependências do projeto incluem:

- [black](https://github.com/psf/black): Formatação de código.
- [faker](https://github.com/joke2k/faker): Geração de dados falsos para testes.
- [flake8](https://github.com/PyCQA/flake8): Ferramenta para linting.
- [httpx](https://www.python-httpx.org/): Biblioteca de requisições HTTP.
- [pytest](https://pytest.org/): Framework de testes.
- [pytest-cov](https://github.com/pytest-dev/pytest-cov): Relatórios de cobertura de testes.
- [pytest-json](https://github.com/nicoddemus/pytest-json): Plugin para saída JSON dos testes.
- [pytest-unordered](https://github.com/altendky/pytest-unordered): Plugin para verificar igualdade de conjuntos de forma não ordenada.
