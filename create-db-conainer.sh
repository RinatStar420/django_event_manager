docker run -d \
    --name test-db \
    -e POSTGRES_USER=shaggy \
    -e POSTGRES_PASSWORD=shaggy \
    -e POSTGRES_DB=test-db \
    -p 5432:5432 \
    postgres

docker container [command] test-db  # выполнять команды для контейнера

psql postgres://name:password@0.0.0.0:5433/db-name  # подключение к бд в контейнере

docker exec -ti container-name [command]  # команда для выполнения внутри контейнера






