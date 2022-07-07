# AirFlowBasicExample

## Set environment
```
# sef container: MySQL, root pwd: root
docker run --name mysql -e MYSQL_ROOT_PASSWORD=joy -p 3306:3306 -d mysql:latest
```

## airflow init
```
pip install apache-airflow

# only install [celery,slack,redis]
pip install apache-airflow[celery,slack,redis]
sudo airflow standalone
```

## Set DB connection
```
# airflow.cfg, modify db connect path
sql_alchemy_conn = mysql+pymysql://DB_USERNAME:DB_PASSWORD@DB_HOST:DB_PORT/DB_database
sql_alchemy_conn = mysql+pymysql://root:joy@0.0.0.0:3306/airflow

# after modified, airflow init again
sudo airflow standalone
```