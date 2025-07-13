# 🦸‍♂️ Superhero API (FastAPI + SQLite)

API для поиска и сохранения супергероев с использованием FastAPI, SQLite и SuperheroAPI.

---

## 🧰 Технологии

| Технология       | Назначение                                      |
|------------------|--------------------------------------------------|
| **Python 3.11+** | Язык программирования                           |
| **FastAPI**      | Веб-фреймворк для создания REST API             |
| **Uvicorn**      | ASGI-сервер для запуска FastAPI-приложения      |
| **SQLite**       | Лёгкая встроенная база данных                   |
| **SQLAlchemy**   | ORM для взаимодействия с базой данных           |
| **Docker**       | Контейнеризация приложения                      |
| **Docker Compose** | Оркестрация сервиса (только API, SQLite встроена) |
| **httpx**        | HTTP-клиент для запросов к SuperheroAPI         |
| **pytest**       | Фреймворк для написания и запуска тестов        |

---

## 🚀 Возможности

- `POST /hero/` — добавить героя по имени из [superheroapi.com](https://superheroapi.com/).
- `GET /hero/` — получить список героев с фильтрацией по атрибутам.
- Хранение данных в SQLite.
- Простая настройка через Docker.
- Тесты на `pytest`.

---

## Структура проекта
<pre>
├── app/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── tests/
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
</pre>

---

## 🔧 Установка и запуск

### 📦 Локально

```bash
git clone https://github.com/Stuspushka/heroapi.git
cd heroapi

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```

### 🐳 Через Docker
```bash
docker-compose up --build
```

---

## 📘 Использование API
✅ Добавить героя

POST /hero/?name=Batman

Параметры:

    name — имя героя (обязательное), ищется в superheroapi.com

🔍 Получить героев

GET /hero/

#### Доступные параметры (все необязательные):
<pre>
Параметр	                              Описание
name	                                точное совпадение по имени
intelligence	                        точное значение интеллекта
intelligence__gte, __lte	        больше/меньше или равно
strength, speed, power и их __gte/__lte	аналогично

Пример:

GET /hero/?strength__gte=80&speed__lte=90
</pre>

---

## 🧪 Тесты

pytest
