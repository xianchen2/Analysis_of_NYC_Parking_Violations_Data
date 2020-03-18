# Analysis_Millions_of_NYC_Parking_Violations

To run:

```
docker-compose build pyth
```

```
docker-compose run -v $(pwd):/app -e APP_TOKEN=$(cat app_token) pyth python get_data.py page_size=100 num_pages=100 output=filename
```

```
docker-compose run pyth python main.py filename
```
