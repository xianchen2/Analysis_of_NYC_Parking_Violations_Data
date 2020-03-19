# Analysis_Millions_of_NYC_Parking_Violations

To run:

```
docker-compose up -d
```


```
docker-compose build pyth
```

```
docker-compose run -v $(pwd):/app -e APP_TOKEN=$(cat app_token) pyth python get_data.py page_size=100 num_pages=100 output=results
```

```
docker-compose run pyth python main.py results
```


```
docker-compose down
```
![ScreenShot](https://github.com/xianchen2/Analysis_Millions_of_NYC_Parking_Violations/blob/master/%20Kibana%20-%20localhost.png)

