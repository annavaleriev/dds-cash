![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/-DRF-ff1709?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white)
![Django ORM](https://img.shields.io/badge/-Django%20ORM-092E20?logo=django&logoColor=white)

##Веб-сервис для управления движением денежных средств (ДДС)
Тестовое задание https://drive.google.com/file/d/146JS1XhWfvCgeCP_SB5fos1YjYPFAWcr/view?usp=sharing

### Описание проекта
Веб-приложение предназначено для ведения учета операций движения денежных средств (ДДС) компании или частного лица.
Сервис позволяет пользователю создавать, редактировать, просматривать и удалять записи о поступлениях и списаниях 
денежных средств, а также управлять справочниками, связанными с этими записями.

Приложение реализует логические зависимости между типами операций, категориями и подкатегориями, 
обеспечивая корректность и достоверность данных.

### Функциональность

📄 Работа с записями о ДДС
Создание записи, включающей:
- дату (автоматически заполняется, но можно изменить вручную),
- статус (например, "Бизнес", "Личное", "Налог"; можно расширять),
- тип (например, "Пополнение", "Списание"; можно расширять),
- категорию и подкатегорию (привязаны друг к другу),
- сумму (в рублях),
- комментарий (необязательный).

Просмотр списка всех записей:
- таблица с фильтрацией по дате, статусу, типу, категории и подкатегории.
- редактирование и удаление любой записи.

🧾 Управление справочниками
Добавление, редактирование и удаление:
- статусов,
- типов,
- категорий,
- подкатегорий.

🔄 Логические зависимости
- подкатегория должна быть привязана к категории.
- категория должна быть привязана к типу.
- при создании записи отображаются только допустимые сочетания.


### Технические требования

- **Язык программирования:** ![Python](https://img.shields.io/badge/Python-3.11-blue)
- **Фреймворк:** ![Django](https://img.shields.io/badge/Django-4.0-green) ![DRF](https://img.shields.io/badge/DRF-3.14-red)
- **База данных:** ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue)
- **ORM:** ![Django ORM](https://img.shields.io/badge/Django%20ORM-ORM-lightblue)
- **Контейнеризация:** ![Docker](https://img.shields.io/badge/Docker-20.10-blue)
- **Валидация данных:** ![Validation](https://img.shields.io/badge/Data%20Validation-Enabled-brightgreen)



## Документация

Документация API доступна по адресу http://127.0.0.1:8000/api/docs/


## Запуск проекта

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/annavaleriev/dds-cash.git

   cd ваш-репозиторий
   
2. Создайте файл .env на основе .env_example и заполните

3. Запустите проект с помощью Docker Compose:
   ```bash
   docker-compose up -d --build
   ```
4. Выполните миграции и создайте суперпользователя (опционально)
   ```bash
   docker-compose exec app python manage.py migrate
   docker-compose exec app python manage.py createsuperuser
   ```
5. Перейдите в браузер по адресу http://127.0.0.1:8000
