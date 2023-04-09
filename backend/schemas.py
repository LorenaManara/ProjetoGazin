from pydantic import BaseModel

class NiveisBase(BaseModel):
    nivel: str
    

class NiveisRequest(NiveisBase):
    ...

class NiveisResponse(NiveisBase):
    id: str

    class Config:
        orm_mode = True


class DesenvolvedoresBase(BaseModel):
    idnivel: str 
    nome: str 
    sexo: str 
    DataNascimento: str 
    idade: int 
    hobby: str 



class DesenvolvedoresRequest(DesenvolvedoresBase):
    ...

class DesenvolvedoresResponse(DesenvolvedoresBase):
    id: str

    class Config:
        orm_mode = True