The aim of this project is to do a first implementation of repository pattern for learning purposes. 

# How to run this project

## Run the database

To put the database up, just run `docker compose up` on the root repository. This command will start a container mapping the data directory from the container to the postgres directory in to app repository. 

## Run the application
To put the application up, just run the following command from the root directory:

```bash
./run.sh
```


When run aplication for the first time, few rows will be inserted into database.

Navigate to `http://127.0.0.1:8080/docs`