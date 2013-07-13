DJ Static
=========

This is a simple Django middleware utility that allows you to properly
serve static assets from production with a WSGI server like Gunicorn.

.. image:: http://farm8.staticflickr.com/7387/8907351990_58677d7c35_z.jpg


Usage
-----

Configure your static assets in ``settings.py``::

   STATIC_ROOT = 'staticfiles'
   STATIC_URL = '/static/'

Then, update your ``wsgi.py`` file to use dj-static::

    from django.core.wsgi import get_wsgi_application
    from dj_static import Cling

    application = Cling(get_wsgi_application())