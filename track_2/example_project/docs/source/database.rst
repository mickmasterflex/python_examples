.. _ref-database-configuration:

====================
Database Configuration
====================

This guide will help you to set up and configure your database.

.. warning::

    These guides assume that you have already created and activated your
    virtualenv.  If you do not activate your virtualenv, the python
    libraries will be installed globally.

PostgreSQL Installation/Configuration (Ubuntu/Debian)
=====================================================

1.  Use your package manager to install the postgres server::

        $ sudo apt-get install postgresql postgresql-contrib libpq-dev

2.  Become the postgresql user, and create a user and database.::

        .. note::

            When it asks if this user should be able to create new databases,
            say yes.

        $ sudo su - postgres
        $ createuser my_project
        $ createdb -O my_project my_project
        $ psql
        postgres=# ALTER USER my_project PASSWORD 'my_project';
        postgres=\q
        $ psql my_project
        my_project=# create extension hstore;
        my_project=# \q


3.  Edit the file **/etc/postgresql/9.1/main/pg_hba.conf** and add the
    following to the bottom of the file::

        local   my_project          my_project    trust
        local   test_my_project     my_project    trust

4.  Reload postgres::

        sudo service postgresql reload
