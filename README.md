# Event management service

DRF project for managing events.

## Installation

```shell
# Clone the repository
git clone https://github.com/b3v3kt0r/event-management

# Set up .env file
You have create .env using .env.sample. like example

# Build docker-compose container
docker-compose build

# Run docker compose
docker-compose up

# Go into docker-container
docker exec -it <container id> sh

# Create super user
python manage.py createsuperuser

# Check it out
http://localhost:8001/user/token

# Or you can use docs:
http://localhost:8000/schema/swagger-ui/
```

## Features

* JWT authenticated.
* CRUD implementation for event management service.
* Filtering for events.
* Docker.
* PostgreSQL.
* Email notification for joining events


## Contact
For contact me:
* Fullname: Stanislav Sudakov
* Email: stanislav.v.sudakov@gmail.com
* Telegram: @sssvvvff