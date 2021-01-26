===================
healthdbModels
===================

**Framework to construct a simple, customizable health database**

This repository is intended to outline a database structure to house clinical data of any type. This database schema is constructed using SQLAlchemy_ and can be modified to suit any business needs.

**Existing Tables**
 Patient
    - Name, Demographics, Address
 Encounter
    - Date(s), Encounter type and description, links to [Organization, Payer, Provider]
 Condition
    - Code and description to link associated
 Medication
    - Medications administered and/or prescribed
 Procedure
    - Procedures performed and their associated codes
 Imaging
    - Overview of imaging performed
 Provider
    - The providers associated with delivery of care
 Organization
    - Organizations from which care was delivered
 Payer
    - Payer organization for which care was delivered

.. _SQLAlchemy: https://www.sqlalchemy.org/