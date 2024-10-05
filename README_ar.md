# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Python Logo" width="52" height="30" />  🍝🦐 Chapa Quente 🍛🥘 - مولد قوائم الطعام <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Python Logo" width="52" height="30" />

## 🌐 
[![Português](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README.md)
[![Español](https://img.shields.io/badge/Español-yellow)](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_es.md)
[![English](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_en.md)
[![Русский](https://img.shields.io/badge/Русский-lightgrey)](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ru.md)
[![中文](https://img.shields.io/badge/中文-red)](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ch.md)
[![العربية](https://img.shields.io/badge/العربية-orange)](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ar.md)

![التعامل مع الفئات في REPL بايثون](./gifs/pythonRestaurant.gif)

تم تطوير هذا المشروع لمطعم **Chapa Quente** بهدف إنشاء أداة فعالة لبناء قوائم الطعام، مع الأخذ في الاعتبار القيود الغذائية للعملاء وتوافر المكونات في المخزون. حاليًا، يتم إدارة الوصفات والمخزون بطريقة غير فعالة من خلال ملفات CSV، وتهدف هذا المشروع إلى حل هذه المشكلة بطريقة أكثر تنظيمًا ووظيفية.

إليك ملخص للأقسام مع تنسيق `h2` كما ترغب:

<details>
<summary><h2>الميزات المنفذة</h2></summary>

- رسم خرائط الأطباق والوصفات.
- مولد قوائم الطعام بناءً على القيود الغذائية وتوافر المكونات.
- إدارة مخزون المكونات.
- تنفيذ اختبارات باستخدام إطار العمل `pytest`.

</details>

<details>
<summary><h2>المهارات التي تم ممارستها</h2></summary>

- استخدام الخرائط المميزة مع Dict و Set.
- اختبارات البرمجيات باستخدام `pytest`.
- تنفيذ الفئات ومبادئ البرمجة الكائنية.

</details>

<details>
<summary><h2>المتطلبات</h2></summary>

- بايثون 3.8 أو أعلى.
- Pip (مدير حزم بايثون).

</details>

<details>
<summary><h2>التثبيت والتنفيذ</h2></summary>

1. استنساخ المستودع.
2. الانتقال إلى دليل المشروع.
3. إنشاء بيئة افتراضية (اختياري).
4. تثبيت التبعيات.
5. تشغيل الاختبارات الآلية.

</details>

<details>
<summary><h2>هيكل الملفات</h2></summary>

```
.
├── src/
│   ├── models/
│   │   ├── dish.py            # تنفيذ فئة Dish
│   │   ├── ingredient.py      # تنفيذ فئة Ingredient
│   │   └── stock.py           # تنفيذ فئة Stock
├── tests/
│   ├── test_dish.py           # اختبارات لفئة Dish
│   ├── test_ingredient.py     # اختبارات لفئة Ingredient
│   └── test_stock.py          # اختبارات لفئة Stock
├── dev-requirements.txt       # التبعيات للتطوير والاختبار
├── requirements.txt           # التبعيات الرئيسية للمشروع
└── README.md                  # توثيق المشروع
```

</details>

<details>
<summary><h2>التبعيات</h2></summary>

- [black](https://github.com/psf/black): تنسيق الكود.
- [faker](https://github.com/joke2k/faker): توليد بيانات وهمية للاختبارات.
- [flake8](https://github.com/PyCQA/flake8): أداة لتحليل الكود.
- [httpx](https://www.python-httpx.org/): مكتبة طلبات HTTP.
- [pytest](https://pytest.org/): إطار عمل للاختبارات.
- [pytest-cov](https://github.com/pytest-dev/pytest-cov): تقارير تغطية الاختبارات.
- [pytest-json](https://github.com/nicoddemus/pytest-json): مكون إضافي للإخراج بصيغة JSON للاختبارات.
- [pytest-unordered](https://github.com/altendky/pytest-unordered): مكون إضافي للتحقق من تساوي المجموعات بشكل غير مرتب.

</details>

<details>
<summary><h2>مشاريع أخرى</h2></summary>

-  [Scripts](https://github.com/SamuelRocha91/scripts/blob/main/README_ar.md)
-  [Algorithms](https://github.com/SamuelRocha91/Algorithms/blob/main/README_ar.md)
-  [Trybe is not google](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

</details>
