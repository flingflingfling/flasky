# flasky
Demo with the flasy tutorial(book).

Flask is a python web microframwork.this is the demo whit flask in python.

## about database
I am a new guy to the coding,so i will follow the introduce.
Here i am using sqlite3 as the database.

# about db-migration
This project will use flask_script to support alembic.

alembic could make the database become easy to migration.

###the code like that:
>python hello.py db migrate -m "initial migration"

upgrade command:
>python hello.py db upgrade

downgrade command:
>python hello.py db downgrade 


