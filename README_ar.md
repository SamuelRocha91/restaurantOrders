# 🍝🦐 Chapa Quente 🍛🥘 - مُوَلِّد القوائم

<h2>🌐</h2>
<ul>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders" target="_blank">Português</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_es.md" target="_blank">Español</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_en.md" target="_blank">English</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ru.md" target="_blank">Русский</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ch.md" target="_blank">中文</a></li>
  <li><a href="https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ar.md" target="_blank">العربية</a></li>
</ul>


![التعامل مع الفئات في Python REPL](./gifs/pythonRestaurant.gif)

تم تطوير هذا المشروع لمطعم **Chapa Quente** بهدف إنشاء أداة فعالة لتوليد القوائم، مع مراعاة القيود الغذائية للعملاء وتوافر المكونات في المخزون. حاليًا، يتم إدارة الوصفات والمخزون بطريقة غير فعالة باستخدام ملفات CSV، ويهدف هذا المشروع إلى حل هذه المشكلة بطريقة أكثر تنظيمًا ووظائف.

## 🛠️ الميزات المنفذة

- **تخطيط الأطباق والوصفات**: تم إنشاء فئة لتخطيط الأطباق والمكونات وكمياتها.
- **مولد القوائم**: تنفيذ فئة مسؤولة عن توليد القوائم بناءً على القيود الغذائية وتوافر المكونات.
- **إدارة المخزون**: تم تنفيذ فئة لإدارة المخزون، لضمان أن الأطباق المتاحة يمكن تحضيرها بالمكونات المتاحة.
- **الاختبارات**: تنفيذ اختبارات باستخدام إطار العمل `pytest`، تغطي وظائف التطبيق مثل التحقق من الأطباق والمكونات والقيود.

## 🚵 المهارات المتدربة

- **استخدام Hashmaps مع Dict وSet**: استخدام هياكل `dict` و `set` في Python لإدارة الأطباق والمكونات.
- **اختبارات البرمجيات**: ممارسة كتابة اختبارات الوحدات للفئات باستخدام `pytest`.
- **البرمجة الكائنية التوجه**: تنفيذ الفئات والأساليب والسمات التي تتبع مبادئ البرمجة الكائنية التوجه.

## 📋 المتطلبات

- Python 3.8 أو أعلى
- Pip (مدير حزم Python)

## 🔧 التثبيت والتشغيل

اتبع الإرشادات أدناه لاستنساخ المشروع وتشغيله على جهازك المحلي:

### 1. استنساخ المستودع

```bash
git clone git@github.com:SamuelRocha91/restaurantOrders.git
```

### 2. انتقل إلى دليل المشروع

```bash
cd restaurantOrders
```

### 3. إنشاء بيئة افتراضية (اختياري، لكنه موصى به)

```bash
python3 -m venv venv
source venv/bin/activate  # على Windows، استخدم: venv\Scripts\activate
```

### 4. تثبيت التبعيات

قم بتثبيت التبعيات المدرجة في ملفات `requirements.txt` و `dev-requirements.txt`:

```bash
pip install -r dev-requirements.txt
```

### 5. تشغيل الاختبارات

لتشغيل الاختبارات التلقائية، استخدم الأمر:

```bash
pytest --cov=src --cov-report=term-missing
```

## 📝 هيكل الملفات

يتم تنظيم هيكل المشروع على النحو التالي:

```
.
├── src/
│   ├── models/
│   │   ├── dish.py            # تنفيذ فئة Dish
│   │   ├── ingredient.py      # تنفيذ فئة Ingredient
│   │   └── stock.py           # تنفيذ فئة إدارة المخزون Stock
├── tests/
│   ├── test_dish.py           # اختبارات لفئة Dish
│   ├── test_ingredient.py     # اختبارات لفئة Ingredient
│   └── test_stock.py          # اختبارات لفئة Stock
├── dev-requirements.txt       # التبعيات للتطوير والاختبارات
├── requirements.txt           # التبعيات الرئيسية للمشروع
└── README.md                  # وثائق المشروع
```

## 📦 التبعيات

تشمل تبعيات المشروع:

- [black](https://github.com/psf/black): تنسيق الشيفرة.
- [faker](https://github.com/joke2k/faker): توليد بيانات وهمية للاختبارات.
- [flake8](https://github.com/PyCQA/flake8): أداة لتحليل الشيفرة.
- [httpx](https://www.python-httpx.org/): مكتبة طلبات HTTP.
- [pytest](https://pytest.org/): إطار عمل للاختبارات.
- [pytest-cov](https://github.com/pytest-dev/pytest-cov): تقارير تغطية الاختبارات.
- [pytest-json](https://github.com/nicoddemus/pytest-json): مكون إضافي لإخراج JSON للاختبارات.
- [pytest-unordered](https://github.com/altendky/pytest-unordered): مكون إضافي للتحقق من المجموعات غير المرتبة.

