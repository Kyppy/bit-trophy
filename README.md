[![Build Status](https://travis-ci.org/Kyppy/bit-trophy.svg?branch=develop)](https://travis-ci.org/Kyppy/bit-trophy) [![Coverage Status](https://coveralls.io/repos/github/Kyppy/bit-trophy/badge.svg?branch=develop)](https://coveralls.io/github/Kyppy/bit-trophy?branch=develop) <a href="https://codeclimate.com/github/Kyppy/bit-trophy/maintainability"><img src="https://api.codeclimate.com/v1/badges/ebc0c1d83631b3a7a78b/maintainability" /></a>

# Bit-trophy
A digital showcase for users to post their personal video game collection.

This project contains resources for the Bit Trophy API. These resources will enable users to create, retrieve, update and delete posts. This API uses a Django DRF framework and a postgreSQL database.

## Motivation ##
<p>Gaming has become not only a massively popular means of entertainment but also an increasingly popular social platform. A frequent but surpsingly tricky question most gamers hear is, "So, what games do you play?". With Bit Trophy you can now show instead of tell using your own personal, virtual video game trophy case.<p>
<p>Users can create and register an account on the Bit Trophy webapp. Using their account they can create a detailed list of all their favorite video game titles. Users can also share their gaming network handles as well as links to their streaming content.<p>

## Frameworks Used ##
**Built With:**
* Python 3.7
* PostgreSQL
* Django 2.1.7

## Features ##
* Users can create and log onto their Bit Trophy account.
* Users can add video game information to their trophy case. This includes titel,genre, a perosnal rating as well as an option to let other users know if you are actively playing the game.
* Users can also share their PSN, Xbox Live, Steam, Twitch and Youtube handles.
* Users can share links to their streaming content.



## Installation ##
Clone the repository:
```
https://github.com/Kyppy/bit-trophy
```

Change into your root directory and create a virtual environment,preferably using pipenv. For example:
```
pipenv shell
```

In the root directory install the dependencies:<br>
**If you are using venv then use:**
```
pip install -r requirements.txt
``` 
**If you are using pipenv use:**
```
pipenv install
```
Install PostgreSQL:
```
(Windows) 
Download and run the PostgreSQL installer: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows
```
```
(Mac OS X) 
Option 1: 
Use a graphical installer such as Postgres.app

Option 2:
Use a package manager such as Homebrew to install Postgres via the command line
Example: brew install postgresql

```

Using Postgres create and ensure the following:
```
1) A postgresql database.A database password is optional but preferred. The database name is not particular.

2) A user/role to access your postgresql database

3) Ensure that the user has permission to access the database as well as create databases. 
```

Create and initialise the following environment variable:
```
DATABASE_URL = psql://<your postgres username>:<your database password>@127.0.0.1:5432/<your database name>
```
## Deployment ##
To run the application change into the root directory and run the following from the command line:
```
1) pipenv shell
2) cd bit_trophy
3) python manage.py runserver
4) Access the app on a browser using http://127.0.0.1:8000/api/games
```

To run the unit tests change into the root directory and run the following from the command line:
```
1) cd bit_trophy
2) python manage.py test
```

If you want to test the API endpoints yourself, you can use the packaged Swagger UI documentation. To access it do the following from the root directory:
```
1) Change directory into 'bit_trophy'
2) run: python manage.py runserver
3) Using a browser access http://127.0.0.1:8000/api/v1/swagger-docs/
```
## HTTP Verbs
| HTTP METHOD      | POST (CREATE)   | GET (READ)                             | PUT (UPDATE)                                                       | DELETE                                                            |
|------------------|-----------------|----------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------|
| v1/games/        | Create new game | Returns all entries from the database. | Error                                                              | Error                                                             |
| v1/game/<int:pk> | Error           | Returns a single game entry.           | If game with specified primary key exists, update. If not, error.  | If game with specified primary key exists, delete. If not, error. |
|                  |                 |                                        |                                                                    |                                                                   |