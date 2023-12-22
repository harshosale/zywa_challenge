
# Zywa-Backend

checkout [here](http://localhost:8888)


## Installation

start server at http://localhost:8888/

```bash
  docker-compose -f docker-compose-dev.yml up -d --build
```

close server at http://localhost:8888/

```bash
  docker-compose -f docker-compose-dev.yml down
```

Running Tests

```bash
  docker-compose -f docker-compose-dev.yml exec zywa_api bash ../test_api.sh
```
