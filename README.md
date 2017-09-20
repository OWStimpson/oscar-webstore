# oscar-webstore
A basic implementation of the Oscar webstore

Running
python manage.py runserver --settings=oscar_webstore_root.settings.dev

Instalation
1) pip install django-oscar
2) pip install unipath
3) pip install django_compressor
4) install postgres and set up db
    a) sudo su - postgres
    b) psql
    c) CREATE DATABASE dbname;
    d) CREATE USER username WITH PASSWORD 'password';
    e) ALTER ROLE username SET client_encoding TO 'utf8';
    f) ALTER ROLE username SET default_transaction_isolation TO 'read committed';
    g) ALTER ROLE username SET timezone TO 'UTC';
    h) GRANT ALL PRIVILEGES ON DATABASE dbname TO username;
5) pip install django psycopg2
6) pip install pycountry
7) python manage.py oscar_populate_countries --no-shipping --settings=oscar_webstore_root.settings.dev
8) edit address_country table and set GB record to allow shipping

Extras
1) A test smtp server can be setup in dev using 'python -m smtpd -n -c DebuggingServer localhost:1025'