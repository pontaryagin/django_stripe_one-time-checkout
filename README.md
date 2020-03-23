# django_stripe_one-time-checkout
Very simple sample Integration of checkout one time payments using stripe. Integrated in March 2020.

This Integration is [based on stripe sample github](https://github.com/stripe-samples/checkout-one-time-payments)

It requires `pipenv` to run the server.

## Steps to run the sample code server

```bash
$ pipenv shell
$ (dev) python manage.py runserver
```

## Directory tree
```bash
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── checkout              # Integrated stripe sample django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── static
│   ├── checkout
│   │   └── js
│   │       └── script.js # Client side javascript
│   ├── css
│   │   ├── bootstrap.min.css
│   │   └── bootstrap.min.css.map
│   └── js
│       ├── bootstrap.bundle.min.js
│       ├── bootstrap.bundle.min.js.map
│       ├── jquery-3.4.1.min.js
│       └── jquery-3.4.1.min.map
├── stripe_test
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates
    ├── base.html
    └── checkout
        ├── canceled.html
        ├── checkout_test.html # Stripe checkout page
        └── success.html
```
