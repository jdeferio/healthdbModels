import datetime as dt
import enum
import uuid

from sqlalchemy import Column, DateTime, Enum, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from healthdbmodels.field_types import UUID, Integer, Telephone

# Define Tables
Base = declarative_base()


class DBMetaData(Base):
    __tablename__ = "db_meta_data"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    task_id = Column(String)
    data_source = Column(String)
    entry_date = Column(DateTime, default=dt.datetime.today)
    target_entity = Column(String)
    target_id = Column(UUID)


class Modality(enum.Enum):
    CT = "CT"
    MR = "MRI"
    PET = "PET"
    XR = "XR"
    US = "US"


class Degree(enum.Enum):
    MD = "MD"
    DO = "DO"
    NP = "NP"


class Patient(Base):
    __tablename__ = "patient"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    last_name = Column(String)
    first_name = Column(String)
    pt_suffix = Column(String)
    birth_date = Column(DateTime)
    death_date = Column(DateTime)
    marital_status = Column(String)
    race = Column(String)
    ethnicity = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String(2))
    zipcode = Column(String(5))

    encounters = relationship("Encounter", back_populates="patient")


class Encounter(Base):
    __tablename__ = "encounter"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    patient_id = Column(UUID, ForeignKey("patient.id"))
    organization_id = Column(UUID, ForeignKey("organization.id"))
    provider_id = Column(UUID, ForeignKey("provider.id"))
    payer_id = Column(UUID, ForeignKey("payer.id"))
    external_id = Column(String, unique=True)
    enc_class = Column(String)
    enc_code = Column(String(9))
    enc_description = Column(String)

    patient = relationship("Patient", back_populates="encounters")
    conditions = relationship("Condition", back_populates="encounter")
    procedures = relationship("Procedure", back_populates="encounter")
    organization = relationship("Organization", back_populates="encounters")
    provider = relationship("Provider", back_populates="encounter")
    payer = relationship("Payer", back_populates="encounters")
    imaging = relationship("Imaging", back_populates="encounter")
    medications = relationship("Medication", back_populates="encounter")


class Organization(Base):
    __tablename__ = "organization"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String(2))
    zipcode = Column(String(5))
    phone = Column(Telephone)

    providers = relationship("Provider", back_populates="organizations")
    encounters = relationship("Encounter", back_populates="organization")


class Condition(Base):
    __tablename__ = "condition"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    encounter_id = Column(UUID, ForeignKey("encounter.id"))
    code = Column(String(9))
    description = Column(String)

    encounter = relationship("Encounter", back_populates="conditions")


class Provider(Base):
    __tablename__ = "provider"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID, ForeignKey("organization.id"))
    name = Column(String)
    degree = Column(Enum(Degree))
    specialty = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String(2))
    zipcode = Column(String(5))

    organizations = relationship("Organization", back_populates="providers")
    encounter = relationship("Encounter", back_populates="provider")


class Imaging(Base):
    __tablename__ = "imaging"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    study_date = Column(DateTime)
    encounter_id = Column(UUID, ForeignKey("encounter.id"))
    modality = Column(Enum(Modality))
    modality_description = Column(String)
    body_part_code = Column(String)
    body_part = Column(String)
    sop_code = Column(String)
    sop_description = Column(String)

    encounter = relationship("Encounter", back_populates="imaging")


class Medication(Base):
    __tablename__ = "medication"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    encounter_id = Column(UUID, ForeignKey("encounter.id"))
    payer_id = Column(UUID, ForeignKey("payer.id"))
    med_code = Column(String(9))
    med_description = Column(String)

    payer = relationship("Payer", back_populates="medications")
    encounter = relationship("Encounter", back_populates="medications")


class Procedure(Base):
    __tablename__ = "procedure"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    date = Column(DateTime)
    encounter_id = Column(UUID, ForeignKey("encounter.id"))
    code = Column(String(9))
    description = Column(String)

    encounter = relationship("Encounter", back_populates="procedures")


class Payer(Base):
    __tablename__ = "payer"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String(2))
    zipcode = Column(String(5))
    phone = Column(Telephone)

    encounters = relationship("Encounter", back_populates="payer")
    medications = relationship("Medication", back_populates="payer")
