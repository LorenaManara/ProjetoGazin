from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# Definição da tabela de níveis
class Nivel(Base):
    __tablename__ = "niveis"

    id = Column(Integer, primary_key=True, index=True)
    nivel = Column(String, index=True)

    # Relacionamento com a tabela de desenvolvedores
    desenvolvedores = relationship("Desenvolvedor", back_populates="nivel")


# Definição da tabela de desenvolvedores
class Desenvolvedor(Base):
    __tablename__ = "desenvolvedores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idNivel = Column(Integer, ForeignKey("niveis.id"))
    sexo = Column(String(1))
    dataNascimento = Column(String(10))
    idade = Column(Integer)
    hobby = Column(String(100))

    # Relacionamento com a tabela de níveis
    nivel = relationship("Nivel", back_populates="desenvolvedores")