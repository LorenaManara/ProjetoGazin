from typing import List, Optional
from pydantic import BaseModel


# Definição do esquema para o modelo Nivel
class NivelBase(BaseModel):
    nivel: str


class NivelCreate(NivelBase):
    pass


class NivelUpdate(NivelBase):
    pass


class NivelOut(NivelBase):
    id: int

    class Config:
        orm_mode = True


# Definição do esquema para o modelo Desenvolvedor
class DesenvolvedorBase(BaseModel):
    nome: str
    idNivel: int


class DesenvolvedorCreate(DesenvolvedorBase):
    sexo: str
    dataNascimento: str
    idade: int
    hobby: str


class DesenvolvedorUpdate(DesenvolvedorBase):
    sexo: Optional[str]
    dataNascimento: Optional[str]
    idade: Optional[int]
    hobby: Optional[str]


class DesenvolvedorOut(DesenvolvedorBase):
    id: int
    sexo: str
    dataNascimento: str
    idade: int
    hobby: str

    class Config:
        orm_mode = True


# Definição do esquema para a lista de desenvolvedores
class DesenvolvedorList(BaseModel):
    __root__: List[DesenvolvedorOut]
