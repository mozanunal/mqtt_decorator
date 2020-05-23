from setuptools import setup, find_packages

desc = """mqtt_decorator is a decorator module which 
converts mqtt subscriptions and messages 
to a [Flask](https://flask.palletsprojects.com/en/1.1.x/) like api."""

long_desc = open("README.md", "r+").read()

setup(
    # Metadata
    name="mqtt_decorator",
    version="0.1.0",
    author=("Mehmet Ozan Unal"),
    author_email="mehmetozanunal@gmail.com",
    url="https://github.com/mozanunal/mqtt_decorator",
    description=desc,
    long_description=long_desc,
    license="GPL",
    # Package info
    packages=["mqtt_decorator", ],
    zip_safe=False,
)
