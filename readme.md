# ДЗ по Bootstrap

## 19.1 

Задание 1 - внести изменения в index.html

Задание 2 - app.py на любой GET запрос запускает index.html

## 19.2

### Задание 1
создано окружение и джанго проект

### Задание 2
- Создайте первое приложение с названием catalog (команда python manage.py startapp catalog)
- Внесите начальные настройки проекта.
  - Какие предварительные настройки необходимо сделать для проекта?
    - Указать папки для статики, (STATICFILES_DIRS)
    - дописать приложения в список установленных приложений, (INSTALLED_APPS)
    - описать точки входа для приложений. (корневой urls.py и urls.py приложения)
    - Где находится точка входа со стороны пользователя в проект?
      - В корневом файле urls.py
- Сделайте настройку урлов (URL-файлов) для нового приложения.

### Задание 3
Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.

https://github.com/oscarbotru/

в папке *приложение*/template

### Задание 4

В приложении в контроллере реализуйте два контроллера:

- Контроллер, который отвечает за отображение домашней страницы.
- Контроллер, который отвечает за отображение контактной информации.
(views.py)

+ add ref to catalog/urls

test: python manage.py runserver

### Доп. задание

Реализуйте обработку сбора обратной связи от пользователя,
который зашел на страницу контактов и отправил свои данные для обратной связи.
(views) - обновить тот же контроллер
(templates + form) - уже написано


