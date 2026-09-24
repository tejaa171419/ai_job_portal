from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.

    All models inherit from this class.
    SQLAlchemy collects their table metadata.
    """

    pass