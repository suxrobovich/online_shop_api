# Online Shop API

Backend на Django REST Framework для интернет-магазина.

## Как запустить

1. Клонировать репозиторий:
   git clone https://github.com/suxrobovich/online_shop_api.git

2. Перейти в папку проекта и создать виртуальное окружение:
   python -m venv venv
   venv\Scripts\activate   (Windows)

3. Установить зависимости:
   pip install -r requirements.txt

4. Применить миграции:
   python manage.py migrate

5. Запустить сервер:
   python manage.py runserver

6. Открыть документацию API:
   http://127.0.0.1:8000/api/docs/

## Возможности
- Регистрация и авторизация (JWT)
- Товары и категории
- Корзина
- Избранное
- Заказы
- Отзывы
