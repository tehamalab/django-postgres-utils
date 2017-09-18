=====
Usage
=====

To use Django Postgres Utils in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_postgres_utils.apps.DjangoPostgresUtilsConfig',
        ...
    )

Add Django Postgres Utils's URL patterns:

.. code-block:: python

    from django_postgres_utils import urls as django_postgres_utils_urls


    urlpatterns = [
        ...
        url(r'^', include(django_postgres_utils_urls)),
        ...
    ]
