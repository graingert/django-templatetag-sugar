DATABASE_ENGINE = 'sqlite3'

INSTALLED_APPS = [
    "django_nose",
    "templatetag_sugar",
    "templatetag_sugar.tests",
]

SECRET_KEY="asdf"

DATABASES = {
    'default': {
        'NAME': 'test.db',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

TEST_RUNNER = 'django_nose.runner.NoseTestSuiteRunner'

