import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250))
    email = Column(String(250), nullable=False)
    password = Column(String(250))
    date_subscription = Column(DateTime(timezone=True))
    

class PersonajeFav(Base):
    __tablename__ = 'personajefav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personaje_name = Column(String(250))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)

class PlanetaFav(Base):
    __tablename__ = 'planetafav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planeta_name = Column(String(250))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)


class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personaje_name = Column(String(250))
    personaje_edad = Column(DateTime(timezone=True))
    personaje_descripcion = Column(String(250))
    personajefav_id = Column(Integer, ForeignKey('personajefav.id'))
    personajefav = relationship(PersonajeFav)

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planeta_name = Column(String(250))
    planeta_localidad = Column(String(250))
    planeta_descripcion = Column(String(250))
    planetafav_id = Column(Integer, ForeignKey('planetafav.id'))
    planetafav = relationship(PlanetaFav)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
