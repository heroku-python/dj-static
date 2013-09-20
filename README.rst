DJ-Static
=========

This is a simple Django middleware utility that allows you to properly
serve static assets from production with a WSGI server like Gunicorn.

Django `doesn't recommend <https://docs.djangoproject.com/en/1.5/howto/static-files/#admonition-serving-the-files>`_
the production use of its static file server for a number of reasons.
There exists, however, a lovely WSGI application aptly named `Static <https://pypi.python.org/pypi/static>`_.

.. image:: http://farm8.staticflickr.com/7387/8907351990_58677d7c35_z.jpg

"Finally, a super-simple way of serving assets in Django that’ll actually perform well" — `@jacobian <https://twitter.com/jacobian/status/356754168075128833>`_

It is suitable for the production use of static file serving, unlike Django.
Enjoy!

Shouldn't I use a CDN?
----------------------

If you have to ask that question, there's actually quite a good chance you don't.
Static responses aren't very different than dynamic ones.

If you're running a top-tier application, optimizing for delivery and reducing
frontend load, you will want to explore using a CDN with
`Django-Storages <http://django-storages.readthedocs.org/en/latest/>`_.


Usage
-----

::

    $ pip install dj-static

Configure your static assets in ``settings.py``::

   STATIC_ROOT = 'staticfiles'
   STATIC_URL = '/static/'

Then, update your ``wsgi.py`` file to use dj-static::

    from django.core.wsgi import get_wsgi_application
    from dj_static import Cling

    application = Cling(get_wsgi_application())

File uploads (optional)
^^^^^^^^^^^^^^^^^^^^^^^

In case you also want to serve media files that were uploaded to ``MEDIA_ROOT``::

    MEDIA_ROOT = 'media'
    MEDIA_URL = '/media/'

Then again, update your ``wsgi.py`` file::

    from django.core.wsgi import get_wsgi_application
    from dj_static import Cling, MediaCling

    application = Cling(MediaCling(get_wsgi_application()))
