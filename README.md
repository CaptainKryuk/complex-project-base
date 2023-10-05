# Установка и настройка бэка
Сначала просто создается джанго проект и нам надо решить
как он будет храниться.

В папке /docker лежат докер файлы для работы с проектом  
/server хранит весь проект  
/requirements соответственно менеджер зависимостей  

Makefile хранит команды для работы с проектом

Сначала нам нужно забилдить образ командой ```make build-backend```  
там исполняется ```docker build -f docker/backend.dockerfile -t products-backend:latest .``` позже
этот образ будет использоваться в docker-compose image
Нам нужен именно ```docker build```, а не ```docker-compose build```, потому что только бэк нам надо сгенерить
включив все папки на уровне ```Makefile```

# Фронт
Создаем приложение в отдельной папке с помощью нового проекта со скаффолдингом
с помощью ```npm create vue@latest```
В появившемся проекте мы меняем vite.config.js -> блок server, чтобы vue можно было запускать как хост
отдельный билд как на бэке нам не нужен, а достаточно будет запустить сервис в docker-compose
брать образ от node и после создания контейнера делать ```npm install && npm run dev```
добавленный в ```make up```

