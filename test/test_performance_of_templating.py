import textwrap
import unittest

import django
import liquid
from django.conf import settings
from django.template import Context
from jinja2 import Environment, DictLoader

from templite import templite


# Intel® Core™ i5-8250U CPU @ 1.60GHz × 8, 16GB RAM, SSD
# Ubuntu 22.04
# Python 3.10.6

# pip3 install Django==4.1.5 Jinja2==3.1.2 python-liquid==1.7.0

class TestPerformanceOfTemplating(unittest.TestCase):
    def setUpClass(self=None) -> None:
        settings.configure(
            TEMPLATES=[
                {"BACKEND": "django.template.backends.django.DjangoTemplates"}
            ]
        )
        django.setup()

    def setUp(self) -> None:
        self.text = (
                "Hello {{name}}!\n" * 50 +
                textwrap.dedent("""\
                {% for node in nodes %}
                    my-{{node}}:
                        vars:
                        config:
                {% endfor %}
                
                {% if name is None %}
                    No name!
                {% endif %}
                """ * 20)
        )

        self.prepare_count = 100
        self.render_count = 1000

        self.name = "World"
        self.nodes = ["node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10"]

    # 131ms
    def test_prepare_templite(self):
        for _ in range(self.prepare_count):
            templite.Templite(self.text)

    # 36ms
    def test_render_templite(self):
        template = templite.Templite(self.text)
        for _ in range(self.render_count):
            template.render({"name": self.name, "nodes": self.nodes})

    # 271ms
    def test_prepare_liquid(self):
        for _ in range(self.prepare_count):
            liquid.Template(self.text)

    # 1sec 200ms
    def test_render_liquid(self):
        template = liquid.Template(self.text)
        for _ in range(self.render_count):
            template.render(name=self.name, nodes=self.nodes)

    # 265ms
    def test_prepare_django(self):
        for _ in range(self.prepare_count):
            django.template.Template(self.text)

    # 1sec 82ms
    def test_render_django(self):
        template = django.template.Template(self.text)
        for _ in range(self.render_count):
            template.render(Context(dict_={"name": self.name, "nodes": self.nodes}))

    # 1sec 446ms
    def test_prepare_jinja(self):
        for _ in range(self.prepare_count):
            env = Environment(loader=DictLoader({"tpl": self.text}), cache_size=0)
            env.get_template("tpl")

    # 67ms
    def test_render_jinja(self):
        env = Environment(loader=DictLoader({"tpl": self.text.replace("None", "none")}), cache_size=0)
        template = env.get_template("tpl")
        for _ in range(self.render_count):
            template.render(name=self.name, nodes=self.nodes)
