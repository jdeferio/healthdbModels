try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='healthdbModels',
    url='https://github.com/jdeferio/healthdbModels',
    author='Joseph Deferio',
    author_email='jdeferio.io@gmail.com',
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
