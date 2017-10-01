# yum_test

## To Run

* create a virtaul enviroment first

  ```virtualenv -p python3 venv```

* activate the virtual enviroment

     ```source venv/bin/activate``` 

* install the required libraries to run

    ``` pip install -r requirements.txt```

* Install postgress

* configure Postgres
    ```sudo su potgres```
    ```createdb mydb```
    ```createuser -P```
    ```psql```

* finally
    ```GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;```




* run the server

    ```python manage.py runserver```

