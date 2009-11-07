from django.template import Template, Context
from django.test import TestCase


class KickassTestCase(TestCase):
    def test_basic(self):
        tmpl = Template("""{% load test_tags %}{% test_tag_1 for "alex" %}""")
        self.assertEqual(tmpl.render(Context()), "alex")
        
        tmpl = Template("""{% load test_tags %}{% test_tag_1 for "brian" as name %}""")
        context = Context()
        tmpl.render(context)
        self.assertEqual(context["name"], "brian")