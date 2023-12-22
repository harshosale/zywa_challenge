
# Zywa-Backend

checkout [here](http://localhost:8888/docs) or
For [postman documentation](https://documenter.getpostman.com/view/27697547/2s9YkrbKaw)


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
For this challenge we have utilised fastAPI with python as it is really a fast way to create light weight apis or microservices.
Beyond the api, basic jwt authentication has been added ```/login```. Also a SUPER ADMIN setup will be done automatically on running the server.
You can login to super admin using ```{"mobile_number": "100000000"}```. Its just a basic setup so only mobile number is used.
Also sample test cases have been added to test data from csv with api response.

Future changes: 
- Authentication can be improved by using passwords or one time passwords or even otps
- Permissions can be added on who can access this endpoint
- If the service is expected to increase heavily then monolith frameworks needs to be considered something like Ruby on Rails, Django or Spring Boot.

