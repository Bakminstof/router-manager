## Менеджер Wi-Fi роутера tp-link N300 модель TL-WR845N

Настойка подключение осуществляется в файле __prod.env__ в каталоге __env__ путём назначения переменных
__APP.ROUTER.HOST__ и __APP.ROUTER.AUTH_TOKEN__. 

__APP.ROUTER.HOST__ - отвечает за шлюз роутера, 
__APP.ROUTER.AUTH_TOKEN__ токен базовой авторизации (берётся из cookie __Authorization__, __без Basic!__)

Сборка и запуск контейнера
```cmd
@SET "APP_HOST=127.0.0.1"
@SET "APP_PORT=30000"

@SET "APP_NAME=router-manager"
@SET "APP_TAG=latest"

@SET "APP_IMAGE=%APP_NAME%:%APP_TAG%"

@SET "ENV_FILE=/src/env/prod.env"

docker build -t %APP_IMAGE% .

docker run -p %APP_HOST%:%APP_PORT%:12000 -e ENV_FILE=%ENV_FILE% --name %APP_NAME% --restart=always -d %APP_IMAGE%
```

Endpoints:
- __GET__ [/wan_ip](http://localhost:30000/wan_ip) - Получение IP адреса в внешней сети ("белый" IP, если между ним и провайдером больше ничего нет)
