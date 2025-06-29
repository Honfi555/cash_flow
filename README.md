# Проект Cash Flow

Это веб-приложение для управления транзакциями, которое позволяет пользователям добавлять, редактировать, фильтровать транзакции, а также управлять справочниками (категории, подкатегории, типы, статусы).

## 1. Установка и настройка

### 1.1. Клонирование репозитория

Сначала клонируйте репозиторий проекта с помощью git:

```bash
  git clone https://github.com/Honfi555/cash_flow.git
  cd cash_flow
```

### 1.2. Установка менеджера пакетов

Установите uv, если он ещё не установлен. Это можно сделать с помощью pip:

```bash
  pip install uv
```

### 1.3. Создание виртуального окружения и загрузка зависимостей

Создайте виртуальное окружение и активируйте его:

```bash
  # Создание виртуального окружения
  uv sync
  
  # Для Windows:
  .venv\Scripts\activate
    
  # Для Linux/Mac:
  source .venv/bin/activate
```

### 1.4. Настройка базы данных (SQLite)

Проект использует базу данных SQLite по умолчанию. Для создания базы данных и таблиц выполните миграции:

```bash
  python manage.py migrate
```

### 1.5. Создание суперпользователя
Для доступа к административной панели Django создайте суперпользователя:

```bash
  python manage.py createsuperuser
```
Введите имя пользователя, email и пароль.

### 1.6. Локальный запуск

```bash
  python manage.py runserver
```