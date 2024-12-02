import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname= Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)


class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)


class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    birth_year = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)


class Favoritos_Personajes(Base):
    __tablename__ = 'favoritos_personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    personajes_id = Column(Integer, ForeignKey('personajes.id'), nullable=False)
    user = relationship(User)
    personajes = relationship(Personajes)


class Favoritos_Planetas(Base):
    __tablename__ = 'favoritos_planetas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    planetas_id = Column(Integer, ForeignKey('planetas.id'), nullable=False)
    user = relationship(User)
    planetas = relationship(Planetas)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
