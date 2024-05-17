# ALTEST

Just a small django app to demostrate how auditlog does not work when setting a JSONField to a literal "null"

See django 4.2 release notes about this:
https://docs.djangoproject.com/en/4.2/releases/4.2/#passing-encoded-json-string-literals-to-jsonfield-is-deprecated


## Versions

Python 3.11.9
Django 4.2.11


## Setup

Basic django setup with virtual env:

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt


## How to reproduce

    python manage.py shell_plus

    In the django shell just do:
        >>> from django.db.models import JSONField, Value
        >>> al = ALModel.objects.create(json_content=Value(None, JSONField()))

