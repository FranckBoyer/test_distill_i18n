# A minimal working example to illustrate problems when using django_distill with i18n_patterns

Tested with `django-4.1.1` and `django_distill-3.0.1`

## Using i18n_patterns in `urls.py`

### Testing in the browser

 * Accessing to `localhost:8000/en/foo/` is perfectly working
 * If we change `LANGUAGE_CODE=en` into `LANGUAGE_CODE=fr` in `setting.py`, then the correct url is now `localhost:8000/fr/foo/`

### Testing django_distill

Using the command
```
python manage.py distill-local --exclude-staticfiles --force output 
```
leads to the following exception
```
django.core.exceptions.ImproperlyConfigured: Using i18n_patterns in an included URLconf is not allowed.
```

## Without using i18n_patterns in `urls.py`

* Uncomment lines 24-26
* Comment lines 29-31


### Testing in the browser

* Accessing to `localhost:8000/foo/` is working as expected.

### Testing django_distill

Using the command
```
python manage.py distill-local --exclude-staticfiles --force output 
```
produces the file `output/foo/index.html` as expected.

