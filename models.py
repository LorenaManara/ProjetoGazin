from sqlalchemy import Column, Integer, String, ForeignKey, Date

from database import Base

class Niveis(Base):
    __tablename__ = "niveis"

    id: int = Column(Integer, primary_key=True, index=True)
    nivel: str = Column(String(100), nullable=False)

class Desenvolvedores(Base):
    __tablename__ = "desenvolvedores"

    id: int = Column(Integer, primary_key=True, index=True)
    idnivel: str = Column(String(100), ForeignKey(Niveis.id), primary_key=True)
    nome: str = Column(String(100), nullable=False)
    sexo: str = Column(String(100), nullable=False)
    DataNascimento: str = Column(Date, nullable=False)
    idade: int = Column(Integer, nullable=False)
    hobby: str = Column(String(100), nullable=False)