## __HealthDB Models__ ##

#### Framework to construct a simple, customizable health database
<br />

__What is it?__ 

healthdbModels is a python package which defines a database structure to house clinical data of any type. This database schema is constructed using [SQLAlchemy](https://www.sqlalchemy.org) and can be modified to suit any business needs. For instance, if your institution uses the [SNOMED-CT](https://www.snomed.org/snomed-ct/five-step-briefing) terminology, the `Encounter`, `Procedure`, `Condition` (Diagnoses), and `Medication` tables could be specificed accordingly.  Simply apply, adjust, or remove the string length restriction for `code` in each corresponding table, and update `term` to the appropriate terminology enum. A list of terminology standards can be found at the following [HIMSS](https://www.himss.org/terminology-standards) page.

Additional tables could be created to house unique terminology definitions, which could reduce the requisite size of each associated table and improve performance. Simply add another class coresponding to your desired terminology (_see_: `healthdb.SNOMED`, `healthdb.RXNORM`), and join on the appropriate `term` and `code` fields.


<br />

__Existing Tables__:
Table Name|Description
:---|:---
`Patient`| Name, Demographics, Address
`Encounter`|Date(s), Encounter type and description, links to [Organization, Payer, Provider]
`Condition`|Code and description to link associated conditions
`Medication`|Medications administered and/or prescribed
`Procedure`|Procedures performed and their associated codes
`Imaging`|Overview of imaging performed
`Provider`|The providers associated with delivery of care
`Organization`|Organizations from which care was delivered
`Payer`|Payer organization for which care was delivered

<br />

A diagram of the HealthDB schema can be found in this [diagrams.net document](https://drive.google.com/file/d/1kQ0O4FJQK0fhrUB3iL3DIrYdoLaji5wV/view?usp=sharing)

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

