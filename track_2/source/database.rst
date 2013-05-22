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

2.  Become the postgresql user, and create a project user and database.::

        .. note::
            
            When it asks if this user should be able to create new databases,
            say yes.

        $ sudo su - postgres
        $ createuser <project_name>
        $ createdb -O <project_name> <project_name>
        $ psql
        postgres=# ALTER USER <project_name> PASSWORD '<project_name>';
        postgres=# \q
        $ psql <project_name>
        <project_name>=# create extension hstore;
        <project_name>=# \q


3.  Edit the file **/etc/postgresql/9.1/main/pg_hba.conf** and add the
    following to the bottom of the file::

        local   <project_name>          <project_name>    trust
        local   test_<project_name>     <project_name>    trust

4.  Reload postgres::
    
        sudo service postgresql reload

5.  Activate your virtualenv and install the required python
    libraries::

        $ pip install psycopg2==2.4.5
