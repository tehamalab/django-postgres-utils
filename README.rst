=============================
Django Postgres Utils
=============================

.. image:: https://badge.fury.io/py/django-postgres-utils.svg
    :target: https://badge.fury.io/py/django-postgres-utils

.. image:: https://travis-ci.org/tehamalab/django-postgres-utils.svg?branch=master
    :target: https://travis-ci.org/tehamalab/django-postgres-utils

.. image:: https://codecov.io/gh/tehamalab/django-postgres-utils/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/tehamalab/django-postgres-utils

UtiliUtilities for Django Postgresql

Quickstart
----------

Install Django Postgres Utils::

    pip install django-postgres-utils

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_postgres_utils',
        ...
    )

Features
--------

* User friendly Admin widget for django HStoreField;
  ``django_postgres_utils.widgets.AdminHStoreWidget``

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
