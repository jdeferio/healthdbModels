import re
import uuid

import pandas as pd
import sqlalchemy.types as types
from sqlalchemy.dialects.postgresql import UUID as psqlUUID


class UUID(types.TypeDecorator):
    """Converts input values to psqlUUID."""

    impl = psqlUUID

    def process_bind_param(self, value, dialect):
        if pd.isnull(value):
            return None
        if not isinstance(value, uuid.UUID):
            if isinstance(value, bytes):
                value = uuid.UUID(bytes=value)
            elif isinstance(value, int):
                value = uuid.UUID(int=value)
            elif isinstance(value, str):
                value = uuid.UUID(value)
        return str(value)

    def process_result_value(self, value, dialect):
        return value


class Integer(types.TypeDecorator):
    """Converts input values to Integer type, accepts np.nan as null value."""

    impl = types.Integer

    def process_bind_param(self, value, dialect):
        if pd.isnull(value):
            return None
        return int(value)

    def process_result_value(self, value, dialect):
        return value


class Telephone(types.TypeDecorator):
    """Converts input values to 10-digit string Ensures that input has exactly
    10 digits If string strips all non-digit characters."""

    impl = types.String

    def process_bind_param(self, value, dialect):
        if pd.isnull(value):
            return None
        if isinstance(value, str):
            value = re.sub("[^\d]", "", value)
        elif isinstance(value, int):
            value = str(value)
        if len(value) == 11 and value[0] == "1":
            value = value[1:]
        if not len(value) == 10:
            raise (ValueError("bad contact field formatting"))
        return value

    def process_result_value(self, value, dialect):
        return value
