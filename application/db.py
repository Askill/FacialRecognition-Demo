import sqlalchemy as db
from sqlalchemy import Column, String, Integer, Numeric, Table, DateTime, ARRAY, ForeignKey, create_engine, LargeBinary, Enum
from sqlalchemy.orm import sessionmaker, relationship, column_property
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import enum
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

engine = db.create_engine('sqlite:///./test.sqlite', echo=True)
connection = engine.connect()
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Gender(enum.Enum):
    other = "other"
    male = "male"
    female = "female"

class Person(Base):
    __tablename__ = "person"
    person_id = Column('person_id', Integer,  primary_key=True, autoincrement=True)
    timestamp = Column('timestamp', DateTime, default=datetime.utcnow)
    fname = Column('fname', String(50))
    lname = Column('lname', String(50))
    yob = Column('yob', Integer)
    gender = Column('gender', Enum(Gender))
    face = Column('face', LargeBinary)
    fingerprints = relationship("Fingerprint", foreign_keys='Fingerprint.person_id')

class Fingerprint(Base):
    __tablename__ = "fingerprint"
    person_id = Column('person_id', Integer, ForeignKey('person.person_id'),  primary_key=True)

    fingerprint_id = Column('fingerprint_id', Integer,  primary_key=True)                       # 0: left pinky;  9: right pinky
    timestamp = Column('timestamp', DateTime, default=datetime.utcnow)
    fingerprint = Column('fingerprint', LargeBinary)

Base.metadata.create_all(engine)