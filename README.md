# Автор
Над проектом работал Афанасьев Александр😌
# Технологии и их версии:
В проекте использовались такие технологии, как:
- asgiref==3.7.2
- certifi==2024.8.30
- cffi==1.15.1
- charset-normalizer==3.4.0
- cryptography==43.0.3
- defusedxml==0.8.0rc2
- Django==3.2.25
- idna==3.10
- oauthlib==3.2.2
- psycopg2==2.9.9
- pycparser==2.21
- PyJWT==2.8.0
- python3-openid==3.2.0
- pytz==2024.2
- requests==2.31.0
- requests-oauthlib==2.0.0
- social-auth-app-django==5.3.0
- social-auth-core==4.4.2
- sqlparse==0.4.4
- typing-extensions==4.7.1
- urllib3==2.0.7

## Как запустить проект:
1. Клонировать репозиторий командой:
```
git clone <ссылка на репозиторий>.
```

2. Создать и активировать виртуальное окружении в корневой директории проекта:
    ```
    python -m venv venv
    ``` 
    
    ```
    source venv/Scripts/activate
    ``` 

3. Установить зависимости командой:
```
pip install -r requirements.txt
```

4. Выполните миграции командой:
```
python manage.py migrate
```

5. Выполните команду для запуска dev-сервера 😹
```
python manage.py runserver
```
