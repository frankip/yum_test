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

* create a super user to download csv

    ```python manage.py createsuperuser```
    
    enter a username and password


* then run the server

    ```python manage.py runserver```

* Go to [site](http://127.0.0.1:8000/)
* to add a new information [add new](http://127.0.0.1:8000/add)

* to download csv got to [admin](http://127.0.0.1:8000/admin/feedform/details/)

