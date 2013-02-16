==========================
Speak Easy Environment Setup
==========================

This guide will help you set up your development environment in order to start
working on your project.  It may also be of use in setting up a production
server.

Linux Installation (Ubuntu/Debian)
==================================

By following these steps, you can easily have a working installation of a
development environment.

.. note::

   The following will assume you are cloning sourcecode to
   **~/Projects/my_project**.  If you are cloning to a different location, you
   will need to adjust these instructions accordingly.

.. note::

   A dollar sign ($) indicates a terminal prompt, as your user, not root.

1.  Clone the source::

        $ cd ~/Projects
        $ git clone git@github.com:ricomoss/python_examples.git

2a. Install some required packages::

        $ sudo apt-get install python python-dev python-pip build-essential

2b. NOTE for Ubuntu: Check to see if you have the following symbolic links::

        $ /usr/lib/libfreetype.so -> /usr/lib/x86_64-linux-gnu/libfreetype.so
        $ /usr/lib/libz.so -> /usr/lib/x86_64-linux-gnu/libz.so
        $ /usr/lib/libjpeg.so -> /usr/lib/x86_64-linux-gnu/libjpeg.so

    If not, ensure you have the following packages::

        $ sudo apt-get install libfreetype6-dev libjpeg8-dev zlib1g-dev

    Then create the symbolic links manually if the system did not do it for you.

3.  Install virtualenv and virtualenvwrapper::

        $ pip install virtualenv
        $ pip install virtualenvwrapper

4.  Add the following to the end of your **~/.bashrc** file::

        source /usr/local/bin/virtualenvwrapper.sh

5.  Type the following::

        $ source /usr/local/bin/virtualenvwrapper.sh

6.  Create your virtualenv::

        $ mkvirtualenv my_project

7.  Add the following to the end of the file
    **~/.virtualenvs/my_project/bin/activate**::

        export DJANGO_SETTINGS_MODULE=my_project.settings.dev
        export PYTHONPATH=$PYTHONPATH:~/Projects/my_project/apps

8.  Activate the virtualenv::

        $ workon my_project

9a.  Install Django 1.5c1::

    Speak Easy will be using Django 1.5c1, which will eventually update to
    Django 1.5.  At which time it will be available as a pip install.
    Until then you need to manually install Django - once Django 1.5 is
    released it will be added to the REQUIREMENTS.pip file mentioned
    below.

        $ pip install https://www.djangoproject.com/download/1.5c1/tarball/

9b.  Install the required python libraries::

        $ pip install -r ~/Projects/my_project/REQUIREMENTS.pip

10. Configure your database (see /docs/source/database.rst).

11. Prepare the database (and add yourself a superuser)::

        $ django-admin.py syncdb
        $ django-admin.py migrate

13. Run the Django development server::

        $ django-admin.py runserver --nostatic

.. note::

    The above command assumes that you're running the runserver your dev
    machine. If you're using a different server for testing, the runserver
    command needs the address to bind to in the format [ipaddress:port].
    For example, if your testing machine's IP is 10.0.0.250, you'd run:

    $ django-admin.py runserver 10.0.0.250:8000 --nostatic

    Any software firewall (e.g. ufw for Ubuntu) would need to allow TCP traffic
    on this port. The following commmand will allow 8000 through ufw:

    $ sudo ufw allow proto tcp from any to any port 8000

14. Copy the address the development server reports that it's running on
    (for example, **http://127.0.0.1:8000/**) and paste it in your browser.

