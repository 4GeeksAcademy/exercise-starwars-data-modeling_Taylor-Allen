import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favourites = relationship('Favourite', backref='user', lazy=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=True)
    length = Column(String(250), nullable=True)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False, unique=True)
    favourites = relationship('Favourite', backref='vehicle', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=True)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    diameter = Column(String(250), nullable=True)
    person = relationship('Person', backref='planet', lazy=True)
    favourites = relationship('Favourite', backref='planet', lazy=True)

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=True)
    hair_color = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    vehicles = relationship('Vehicle', backref='person')
    favourites = relationship('Favourite', backref='person', lazy=True)

class Favourite(Base):
    __tablename__ = 'favourite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=True)

    def to_dict(self):
        return {}
    


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
