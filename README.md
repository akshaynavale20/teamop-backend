# EVSLocator
A EVS (Electric Vehicle Station) Locator developed using the Django Rest API Framework.

## Setup evslocator
### Required steps to run services

#### Git clone repo
> - [x] ```git clone https://github.com/akshaynavale20/teamop-backend.git ~/evslocator```
> - [x] ```cd ~/evslocator```

#### Create Virtualenv
> - [x] ```virtualenv ~/virt/evslocator -p python3```

#### Activate Virtualenv
> - [x] ```source ~/virt/evslocator/bin/activate```

#### Install Required PIP Packages
> - [x] ```pip install -U -r requirements.txt```


## Setup DB
#### Setup Database using Django ORM
> - [x] ```cd ~/evslocator/src```
> - [x] ```python manage.py makemigrations```
> - [x] ```python manage.py migrate```

### Start Service
> - [x] ```python manage.py runserver```


### Create A superuser for Django Admin Panel
#### To access the DB Tables and manipulate it is data from Admin Panel.
> - [x] ```python manage.py createsuperuser```

 
##### As you can see now wallet.sqlite3 file is created for our DB Operations.
##### Time to spare this.!!

## Import Postman Collection Using Below Link.
https://www.getpostman.com/collections/805c23fa94f778885969


