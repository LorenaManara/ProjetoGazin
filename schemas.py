from pydantic import BaseModel

class NiveisBase(BaseModel):
    id: int
    nivel: str
    

class NiveisRequest(NiveisBase):
    ...

class NiveisResponse(NiveisBase):
    id: int

    class Config:
        orm_mode = True


class DesenvolvedoresBase(BaseModel):
    id: int 
    idnivel: str 
    nome: str 
    sexo: str 
    DataNascimento: str 
    idade: int 
    hobby: str 

class DesenvolvedoresRequest(DesenvolvedoresBase):
    ...

class DesenvolvedoresResponse(DesenvolvedoresBase):
    id: int

    class Config:
        orm_mode = True