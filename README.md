# Дипломный проект. Часть 2 — API-тестирование Stellar Burgers

## Описание
Проект представляет собой автоматизированные тесты API для сервиса **Stellar Burgers**.  
Тестируется следующий функционал:
- регистрация пользователя;
- логин пользователя;
- создание заказа с разными условиями.

Проект построен с использованием `pytest`, `requests`, `allure-pytest` и оформлен с генерацией Allure-отчета.

---

### Установите зависимости:
```bash
pip install -r requirements.txt
```

---

## Запуск тестов

### Прогон всех тестов:
```bash
pytest tests/
```

### Прогон с генерацией Allure-отчета:
```bash
pytest tests/ --alluredir=allure-results
allure generate allure-results --clean -o allure-report
allure open allure-report
```

##  Структура проекта

```
Diplom_2/
├── tests/                    # Тесты по API
│   ├── test_create_user.py
│   ├── test_login_user.py
│   └── test_create_order.py
├── conftest.py               # Фикстуры Pytest
├── data.py                   # Тестовые данные и генераторы
├── urls.py                   # Константы с адресами API
├── requirements.txt
├── pytest.ini
└── README.md
```

---
