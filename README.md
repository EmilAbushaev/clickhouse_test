# clickhouse_test
Это тестовое задание, в котором использовалась СУБД Clickhous. 
Необходимо было найти первые 100 наиболее часто встречающихся слов в таблице. 
Поиск осуществлялся по столбцу 'text'.

# Используемые технологии и библиотеки:
* Python 3.11
* fastapi~=0.104.1
* uvicorn==0.24.0.post1
* sqlalchemy~=1.4.50
* clickhouse-driver==0.2.6


# Установка и настройки

### Создание и активирование виртуального окружения:
```
python -m venv env
```
```
source venv/Scripts/activate
``` 
### Установка зависимостей:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
### Скачать контейнер докер:
```
docker pull bitnami/clickhouse:latest
```
### Запуск контейнера, указать порт 9000. Пароль 'click':
```
docker run --name clickhouse -p 9000:9000 -e CLICKHOUSE_ADMIN_PASSWORD=click bitnami/clickhouse:latest

```
### Отправка файла базы данных в контейнер:
```
docker cp ./lenta-ru-news.csv clickhouse:/

```
### Запуск сервиса main.py:
```
python main.py

```
### Запуск клиента в контейнере и заполнение из файла csv:
```
docker exec -it clickhouse clickhouse-client

```
```
clickhouse-client -q "INSERT INTO lenta_ru_news FORMAT CSV" < lenta-ru-news.csv
```
### Запуск uvicorn из директории main.py:
```
uvicorn main:app --reload
```
# Документация:
```
`http://127.0.0.1:8000/docs/`
```
