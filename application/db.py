import sqlalchemy as db
from sqlalchemy import Column, String, Integer, Numeric, Table, DateTime, ARRAY, ForeignKey, create_engine, LargeBinary, Enum
from sqlalchemy.orm import sessionmaker, relationship, column_property
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import enum
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import application.config as config

engine = db.create_engine('sqlite:///' + config.databaseFile, echo=config.echoDatabase)
connection = engine.connect()
Base = declarative_base()
Session = sessionmaker(bind=engine)

lastImage = ""

class Gender(enum.Enum):
    other = "Other"
    male = "Male"
    female = "Female"
    def __str__(self):
        return str(self.value)

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

    def serialize(self):
        prints = []
        for fingerprint in self.fingerprints:
            prints.append(fingerprint.serialize())
        
        if self.face is not None:
            face = self.face.decode('utf-8')
        else:
            face = None

        data = {
        "person_id": self.person_id,
        "timestamp": self.timestamp,
        "fname": self.fname,
        "lname": self.lname,
        "yob": self.yob,
        "gender": str(self.gender),
        "face": face,
        "fingerprints": prints
        }
        return data

class Fingerprint(Base):
    __tablename__ = "fingerprint"
    person_id = Column('person_id', Integer, ForeignKey('person.person_id'),  primary_key=True)

    fingerprint_id = Column('fingerprint_id', Integer,  primary_key=True)                       # 0: left pinky;  9: right pinky
    timestamp = Column('timestamp', DateTime, default=datetime.utcnow)
    fingerprint = Column('fingerprint', LargeBinary)

    def serialize(self):
        if self.fingerprint is not None:
            fp = self.fingerprint.decode('utf-8')
        else:
            fp = None
        data = {
            "person_id": self.person_id,
            "fingerprint_id": self.fingerprint_id,
            "timestamp": self.timestamp,
            "fingerprint": fp
        }
        return data

Base.metadata.create_all(engine)