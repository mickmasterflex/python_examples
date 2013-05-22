Testing
=======
Testing is an important part of the Maintainability of Python projects.
Focus on building automated testing for models, forms and other classes with
commonly-used and/or vital interfaces for the functions of your project. With these
efforts, strive to keep as close as we can to 100% code coverage in these
tested areas.

In Your Project
---------
.. warning::
    These guides assume that you have already created and activated your
    proton virtualenv.  If you do not activate your virtualenv, the python
    libraries will be installed globally.

We use Django's test commands to execute tests. There is only one
adjustment that needs to be made to the standard command; Use the test settings
included in the repository.::

    $ django-admin.py test --settings=<your_project>.settings.test

This will test all apps within your project. However usually as you are developing,
you will want to be specific to the app you modifying. Through Django's test
command, you can also define the specific app to test with the following
command.::

    $ django-admin.py test <specific_app> --settings=<your_project>.settings.test

Notes
-----
You should always require that tests be ran before pushing code live. If you push
code that breaks tests, this will most likely cause other developers to stall their
changes until they can fully test their changes.

There are often exceptions for testing. Templates and Views in Django are
not difficult or impossible to test (in some situations). Both of these areas have
often changing interfaces that really hamper development.  So it is often accepted
to avoid rigid testing for Templates and Views.

