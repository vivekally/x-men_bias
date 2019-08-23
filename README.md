# django_base

This is a Django project template which can be forked to build Django apps in the future.

## Why django_base

This template can be used by developers going forward to save time and make sure you don't miss adding any critical components.

***

## What does it have

* Logging
* Sentry
* Datadog Integration
* Celery Integration
* Django origin trail
* Serve Staticfiles

***

## How to make it my own

* Start with renaming the project and **replacing EVERY occurence** of "mimir" to your project name (case sensitive)
* Update SECRET_KEY with a random 50 letter key. This has to be different for Production, Staging and Development. You can use this [Web Tool](https://www.miniwebtool.com/django-secret-key-generator/) to generate secret keys.
* Here, docker-compose is just a template. Update this with services you need to get your project up and running.
* Update sentry project DSN.
* Update Service Trail and add service trail in development and staging as well.

***
***

### Side note

Suggestions and Contributions are always welcome.
