# -*- coding: utf-8 -*-
"""
dj-static
~~~~~~~~~

This is a simple Django middleware utility that allows you to properly
serve static assets from production with a WSGI server like Gunicorn.

Usage
-----

Configure your static assets in ``settings.py``::

   STATIC_ROOT = 'staticfiles'
   STATIC_URL = '/static/'

Then, update your ``wsgi.py`` file to use dj-static::

    from django.core.wsgi import get_wsgi_application
    from dj_static import StaticCling

    application = StaticCling(get_wsgi_application())

"""

from setuptools import setup

setup(
    name='dj-static',
    version='0.0.5',
    url='https://github.com/kennethreitz/dj-static',
    license='BSD',
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    description='Serve production static files with Django.',
    long_description=__doc__,
    py_modules=['dj_static'],
    zip_safe=False,
    install_requires=['static'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
