# Power

yet another discord bot this time with a cassandra backend

## Startup Cassandra

docker build -t power-cassandra .
docker run -dp 9042:9042 power-cassandra
docker exec -it $(docker inspect --format '{{ .ID }}' power-cassandra) bash

## Startup Power

echo "{ \
 "token": "", \
 "aoc_cookie": "", \
 "aoc_lb": "", \
 "dev": "", \
 "trusted": [] \
 }" > config.json

python3 ./src/main.py
