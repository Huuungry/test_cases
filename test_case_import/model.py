from sqlalchemy import  ForeignKey
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class TestCasesMetadata(Base):
    __tablename__ = 'TEST_CASES_METADATA'
    ID = Column(Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    TEST_CASE_NAME = Column(String(100), unique=True)
    PRECONDITION = Column(String(100))
    ATTACHMENTS = Column(String(100))
    PRIORITY = Column(String(100))
    TestCasesDetails = relationship("TestCasesDetails",  cascade="all, delete, delete-orphan")


class TestCasesDetails(Base):
    __tablename__ = 'TEST_CASE_DETAILS'
    ID = Column(Integer, primary_key=True)
    TEST_CASE_ID = Column(Integer, ForeignKey('TEST_CASES_METADATA.ID'))
    STEP_NUMBER = Column(Integer)
    DESCRIPTION = Column(String(100))
    EXPECTED_RESULT = Column(String(100))
    ACTUAL_RESULT = Column(String(100))
    STATUS = Column(String(100))
    SCREENSHOT = Column(BYTEA)


