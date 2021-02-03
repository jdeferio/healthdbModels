try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

DISTNAME = "healthdbModels"
AUTHOR = "Joseph Deferio"
EMAIL = "jdeferio.io@gmail.com"
DESCRIPTION = "Framework to construct a simple, customizable health database"
URL = "https://github.com/jdeferio/healthdbModels"

setup(
    name=DISTNAME,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    packages=['healthdbmodels'],
    install_requires=[
        'pandas', 
        'sqlalchemy',
        ],
    version='0.1.0',
    license='LICENSE.txt',
    description='Framework to construct a simple, customizable health database',
    long_description=open('README.rst').read(),
)
