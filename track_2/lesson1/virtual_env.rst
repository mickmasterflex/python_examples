.. _virtual-environment-setup:

==========================
Environment Setup
==========================

This guide will help you set up your virtual environment.

Linux Installation (Ubuntu/Debian)
==================================

By following these steps, you can easily create a virtual environment and setup a database for your Django project.

.. attention::  **A dollar sign ($) indicates a terminal prompt, as your user, not root.**

1.  Install some required packages::

        $ sudo apt-get install python python-dev python-pip

2.  Install virtualenv and virtualenvwrapper::

        $ pip install virtualenv
        $ pip install virtualenvwrapper

3.  Add the following to the end of your **~/.bashrc** file::

        source /usr/local/bin/virtualenvwrapper.sh

4.  Type the following::

        $ source /usr/local/bin/virtualenvwrapper.sh

5.  Create your new virtualenv::

        $ mkvirtualenv <virtual_env_name>

6.  Activate the proton virtualenv::

        $ workon <virtual_env_name>

7.  Install the required python libraries for your project::

        $ pip install -r ~/python_class/my_site/REQUIREMENTS.pip

8.  Configure your database::

        $ sudo apt-get install postgresql postgresql-contrib libpq-dev

9.  Become the postgres user and create a project user and database::

        $ sudo su - postgres
        $ createuser <project_username>
        $ createdb -O <project_username> <project_name>
        $ psql <project_username>

10. Edit the file **/etc/postgresql/9.1/main/pg_hba.conf** and add the following to the bottom of the file::

        local    <project_username>    <db_name>    trust

11. Reload postgres::

        $ sudo service postgresql reload

12. Run the Django development server::

        $ django-admin.py runserver

13. Copy the address the development server reports that it's running on
    (for example, **http://127.0.0.1:8000/**) and paste it in your browser.
