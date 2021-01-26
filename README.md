## __HealthDB Models__ ##

#### Framework to construct a simple, customizable health database
<br />

__What is it?__ 

healthdbModels is a python package to outline a database structure to house clinical data of any type. This database schema is constructed using [SQLAlchemy](https://www.sqlalchemy.org) and can be modified to suit any business needs.

<br />

__Existing Tables__:
- Patient
    - Name, Demographics, Address
- Encounter
    - Date(s), Encounter type and description, links to [Organization, Payer, Provider]
- Condition
    - Code and description to link associated
- Medication
    - Medications administered and/or prescribed
- Procedure
    - Procedures performed and their associated codes
- Imaging
    - Overview of imaging performed
- Provider
    - The providers associated with delivery of care
- Organization
    - Organizations from which care was delivered
- Payer
    - Payer organization for which care was delivered

<br />

__Where to get it:__

The source code is currently hosted on GitHub at:
https://github.com/jdeferio/healthdbModels

Binary installers for the latest released version are _not_ currently available, but the package can be installed using either [Pip](https://pip.pypa.io/en/stable/), [Poetry](https://python-poetry.org) or a package manager of your choosing. 

```sh
# pip
pip install git+https://www.github.com/jdeferio/healthdbModels
```

```sh
# or poetry
poetry add git+https://www.github.com/jdeferio/healthdbModels
```
<br />

__Dependencies:__

- [Pandas - allows for efficient declaration of field types](https://github.com/pandas-dev/pandas)
- [SQLAlchemy - allows the user to interact with the ORM on which the database is modeled](https://www.sqlalchemy.org)

<br />

__License:__ [MIT](LICENSE.txt)

