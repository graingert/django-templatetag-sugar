from django.db import models
import six


def python_2_unicode_compatible(klass):
    """
A decorator that defines __unicode__ and __str__ methods under Python 2.
Under Python 3 it does nothing.

To support Python 2 and 3 with a single code base, define a __str__ method
returning text and apply this decorator to the class.
"""
    if not six.PY3:
        klass.__unicode__ = klass.__str__
        klass.__str__ = lambda self: self.__unicode__().encode('utf-8')
    return klass


@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
