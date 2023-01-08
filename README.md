# Python Frameworks

- Jinja2 3.1.2 <https://jinja.palletsprojects.com/en/3.0.x/>
- Django 4.1.5 <https://docs.djangoproject.com/en/4.1/topics/templates/>
- Python Liquid 1.7.0 <https://jg-rp.github.io/liquid/introduction/getting-started>
- Templite (prototype by Ned Batchelder) <http://aosabook.org/en/500L/a-template-engine.html>

`pip3 install Jinja2==3.1.2 Django==4.1.5 python-liquid==1.7.0`

# Source

- [test_performance_of_templating.py](test/test_performance_of_templating.py)
- [test_performance_of_file_writing.py](test/test_performance_of_file_writing.py)
- [templite.py](templite/templite.py)

# Performance Test Results

| Framework     | 100x Preparation/Compilation | 1000x Rendering  |
|---------------|------------------------------|------------------|
| Jinja2        | 1sec 446ms                   | 67ms             |
| Django        | 265ms                        | 1sec 82ms        |
| Python Liquid | 271ms                        | 1sec 200ms       |
| Templite      | 131ms                        | 36ms             |
