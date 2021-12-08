from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

desc = """mqtt_decorator is a decorator module which 
converts mqtt subscriptions and messages 
to a Flask like api."""

long_desc = open("README.md", "r+").read()

setup(
    # Metadata
    name="mqtt_decorator",
    version="0.1.4",
    install_requires=requirements,
    author=("Mehmet Ozan Unal"),
    author_email="mehmetozanunal@gmail.com",
    maintainer="Mehmet Ozan Unal",
    maintainer_email='mehmetozanunal@gmail.com',
    url="https://github.com/mozanunal/mqtt_decorator",
    platforms=["all"],
    description=desc,
    long_description=long_desc,
    long_description_content_type='text/markdown',
    license="GPL",
    # Package info
    packages=["mqtt_decorator", ],
    zip_safe=False,
)
