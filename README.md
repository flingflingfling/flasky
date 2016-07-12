# flasky
Demo with the flasy tutorial(book).

Flask is a python web microframwork.this is the demo whit flask in python.

## about database
I am a new guy to the coding,so i will follow the introduce.
Here i am using sqlite3 as the database.

# about db-migration
This project will use flask_script to support alembic.

alembic could make the database become easy to migration.

###the code likes that:
>python manage.py db init  >>initialize the migration

create database 
>python manage.py shell
> '>>>from app import db
> '>>>db.create_all()
> '>>>exit
>python manage.py upgrade

upgrade command:    # create tables or upgrade to the latest .
>python hello.py db upgrade

downgrade command:
>python hello.py db downgrade 

##about permission
put the roles into db
>python manage.py shell
>>>Role.insert_roles()
>>>ROle.query.all()


flask pacakage intro:
• PageDown:使用 JavaScript 实现的客户端 Markdown 到 HTML 的转换程序。
• Flask-PageDown:为 Flask 包装的 PageDown,把 PageDown 集成到 Flask-WTF 表单中。
• Markdown:使用 Python 实现的服务器端 Markdown 到 HTML 的转换程序。
• Bleach:使用 Python 实现的 HTML 清理器

