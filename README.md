# Yoloco FastAPI
Yoloco FastAPI - это API с двумя эндпоинтами. 
С помощью эндпоинта *'/add_user/{username}'* по юзернейму можно собирать инфо об IG аккаунте и о необходимом количестве постов юзера.
Результат сохраняется в PostgreSQL. 
С помощью второго эндпоинта *'/get_user/{username}'* по юзернейму можно получать данные об аккаунте юзера и о всех сохраненных в базе данных постах.


### Установка
Для установки и запуска необходимо сделать следующее:
1. Клонировать репозиторий с github<br/> 
`git clone https://github.com/Rubinumka23/test_task.git`
2. Создать виртуальное окружение
3. Установить зависимости<br/>
`pip install -r requirements.txt`
4. В корне проекта создать файл .env и добавить переменные:
```
HOST_DB='Имя хоста'
POSTGRES_USER='Логин базы данных'
POSTGRES_PASSWORD='Пароль базы данных'
POSTGRES_DB='Название базы данных'
PROXY=http://Логин:Пароль@Сервер:Порт/
```
5. Запустить скрипт командой<br/>
`docker-compose up`