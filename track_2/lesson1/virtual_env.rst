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

        $ mkvirtualenv python_class

6.  Add the following to the end of the file
    **~/.virtualenvs/proton/bin/activate**::

        export DJANGO_SETTINGS_MODULE=todo.settings.dev
        export PYTHONPATH=$PYTHONPATH:~/python_class/my_site/my_site/apps

7.  Activate the proton virtualenv::

        $ workon python_class

8.  Install the required python libraries for your project::

        $ pip install -r ~/python_class/my_site/REQUIREMENTS.pip

9.  Configure your database::

        $ sudo apt-get install postgresql postgresql-contrib libpq-dev

10.  Become the postgres user and create a project user and database::

        $ sudo su - postgres
        $ createuser <project_username>
        $ createdb -O <project_username> <project_name>
        $ psql <project_username>

11.  Edit the file **/etc/postgresql/9.1/main/pg_hba.conf** and add the following to the bottom of the file:

        local    <project_username>    <db_name>    trust

12.  Reload postgres:

        $ sudo service postgresql reload

13. Run the Django development server::

        $ django-admin.py runserver

14. Copy the address the development server reports that it's running on
    (for example, **http://127.0.0.1:8000/**) and paste it in your browser.
