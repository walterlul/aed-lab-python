from sqlalchemy import Column, Integer, String, Float
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    usuario = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    rol = Column(String, default="cliente")


class Bicicleta(Base):
    __tablename__ = "bicicletas"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    color = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    precio_hora = Column(Float, nullable=False)
    estado = Column(String, default="Disponible")