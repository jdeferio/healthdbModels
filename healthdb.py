import datetime as dt
import enum
import uuid

from sqlalchemy import (
    JSON,
    CheckConstraint,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    SmallInteger,
    String,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from healthdbModels.db_types import UUID, Integer, Telephone

# Define Tables
Base = declarative_base()


class DBMetaData(Base):
    __tablename__ = "db_meta_data"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    task_id = Column(String)
    data_source = Column(String)
    entry_date = Column(DateTime, default=dt.datetime.today())
    target_entity = Column(String)
    target_id = Column(UUID)


class Patient(Base):
    __tablename__ = "patient"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    pt_lastname = Column(String)
    pt_firstname = Column(String)
    pt_suffix = Column(String)
    pt_dob = Column(DateTime)
    pt_death = Column(DateTime)
    pt_marital = Column(String)
    pt_race = Column(String)
    pt_ethnicity = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(String(5))

    __mapper_args__ = {"polymorphic_identity": "patient"}


class Encounter(Base):
    __tablename__ = "encounter"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    patient_id = Column(UUID, ForeignKey("patient.id"), index=True)
    organization_id = Column(UUID, ForeignKey("organization.id"), index=True)
    provider_id = Column(UUID, ForeignKey("provider.id"), index=True)
    payer_id = Column(UUID, ForeignKey("payer.id"), index=True)
    enc_class = Column(String)
    enc_code = Column(String(9))
    enc_description = Column(String)
    condition_id = Column(UUID, ForeignKey("condition.id"), index=True)


class Organization(Base):
    __tablename__ = "organization"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    name = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String(2))
    zipcode = Column(String(5))
    phone = Column(Telephone)


class Payer(Base):
    __tablename__ = "payer"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    name = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String(2))
    zipcode = Column(String(5))
    phone = Column(Telephone)


class Provider(Base):
    __tablename__ = "provider"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    organization_id = organization_id = Column(
        UUID, ForeignKey("organization.id"), index=True
    )
    name = Column(String)
    gender = Column(String)
    specialty = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String(2))
    zipcode = Column(String(5))


class Imaging(Base):
    __tablename__ = "imaging"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    study_date = Column(DateTime)
    patient_id = Column(UUID, ForeignKey("patient.id"), index=True)
    encounter_id = Column(UUID, ForeignKey("encounter.id"), index=True)
    modality = Column(String)
    modality_description = Column(String)
    body_part_code = Column(String)
    body_part = Column(String)
    sop_code = Column(String)
    sop_description = Column(String)


class Condition(Base):
    __tablename__ = "condition"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    code = Column(String, ForeignKey("encounter.code"), unique=True)
    description = Column(String)


class Medication(Base):
    __tablename__ = "medication"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    patient_id = Column(UUID, ForeignKey("patient.id"), index=True)
    encounter_id = Column(UUID, ForeignKey("encounter.id"), index=True)
    payer_id = Column(UUID, ForeignKey("payer.id"), index=True)
    med_code = Column(String)
    med_description = Column(String)
    condition_id = Column(UUID, ForeignKey("condition.id"), index=True)
