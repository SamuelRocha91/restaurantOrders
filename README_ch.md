# 🍝🦐 Chapa Quente 🍛🥘 - 菜单生成器

<h2>🌐</h2>
<ul>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders" target="_blank">Português</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_es.md" target="_blank">Español</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_en.md" target="_blank">English</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ru.md" target="_blank">Русский</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ch.md" target="_blank">中文</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ar.md" target="_blank">العربية</a></li>
</ul>


![在 Python REPL 中处理类](./gifs/pythonRestaurant.gif)

该项目是为餐厅 **Chapa Quente** 开发的，旨在创建一个有效的菜单生成工具，考虑客户的饮食限制和库存中食材的可用性。目前，配方和库存管理通过 CSV 文件以低效的方式进行，此项目旨在通过更有组织和功能性的方式解决此问题。

## 🛠️ 实现的功能

- **菜品和配方映射**: 创建了一个类来映射菜品及其相应的食材和数量。
- **菜单生成器**: 实现了一个类，负责根据饮食限制和食材的可用性生成菜单。
- **库存管理**: 实现了一个类，用于管理食材库存，确保可用的菜品可以用库存中的食材准备。
- **测试**: 使用 `pytest` 框架实现了测试，涵盖了应用程序的功能，例如菜品、食材和限制的验证。

## 🚵 培训的技能

- **使用 Dict 和 Set 的哈希映射**: 使用 Python 的 `dict` 和 `set` 结构来管理菜品和食材。
- **软件测试**: 实践使用 `pytest` 为类编写单元测试。
- **面向对象编程**: 实现类、方法和属性，遵循面向对象编程的原则。

## 📋 要求

- Python 3.8 或更高版本
- Pip (Python 包管理器)

## 🔧 安装与运行

按照以下说明在本地计算机上克隆并运行项目：

### 1. 克隆仓库

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. 导航到项目目录

```bash
cd your-repository
```

### 3. 创建虚拟环境 (可选，但建议)

```bash
python3 -m venv venv
source venv/bin/activate  # 在 Windows 上，使用: venv\Scripts\activate
```

### 4. 安装依赖项

安装 `requirements.txt` 和 `dev-requirements.txt` 文件中列出的依赖项：

```bash
pip install -r dev-requirements.txt
```

### 5. 运行测试

要运行自动化测试，请使用以下命令：

```bash
pytest --cov=src --cov-report=term-missing
```

## 📝 文件结构

项目的文件结构如下：

```
.
├── src/
│   ├── models/
│   │   ├── dish.py            # 菜品类的实现
│   │   ├── ingredient.py      # 食材类的实现
│   │   └── stock.py           # 库存管理类的实现
├── tests/
│   ├── test_dish.py           # 菜品类的测试
│   ├── test_ingredient.py     # 食材类的测试
│   └── test_stock.py          # 库存类的测试
├── dev-requirements.txt       # 开发和测试的依赖项
├── requirements.txt           # 项目的主要依赖项
└── README.md                  # 项目文档
```

## 📦 依赖项

项目的依赖项包括：

- [black](https://github.com/psf/black): 代码格式化。
- [faker](https://github.com/joke2k/faker): 用于测试的虚假数据生成。
- [flake8](https://github.com/PyCQA/flake8): 代码检查工具。
- [httpx](https://www.python-httpx.org/): HTTP 请求库。
- [pytest](https://pytest.org/): 测试框架。
- [pytest-cov](https://github.com/pytest-dev/pytest-cov): 测试覆盖率报告。
- [pytest-json](https://github.com/nicoddemus/pytest-json): 生成 JSON 格式测试输出的插件。
- [pytest-unordered](https://github.com/altendky/pytest-unordered): 用于无序集的相等性检查的插件。


