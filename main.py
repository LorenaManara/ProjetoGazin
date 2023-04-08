from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models import Niveis, Desenvolvedores
from database import engine, Base, get_db
from repositories import NiveisRepository, DesenvolvedoresRepository 
from schemas import NiveisRequest, NiveisResponse, DesenvolvedoresRequest,  DesenvolvedoresResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Código inicial do arquivo omitido para facilitação da leitura

@app.post("/api/niveis", response_model=NiveisResponse, status_code=status.HTTP_201_CREATED)
def create_Niveis(request: NiveisRequest, db: Session = Depends(get_db)):
    nivel = NiveisRepository.save(db, Niveis(**request.dict()))
    return NiveisResponse.from_orm(nivel)


# Código inicial do arquivo omitido para facilitação da leitura

@app.get("/api/niveis", response_model=list[NiveisResponse])
def find_all_Niveis(db: Session = Depends(get_db)):
    niveis = NiveisRepository.find_all(db)
    return [NiveisResponse.from_orm(niveis) for niveis in niveis]

# Código inicial do arquivo omitido para facilitação da leitura

@app.get("/api/niveis/{id}", response_model=NiveisResponse)
def find_by_id_Niveis(id: int, db: Session = Depends(get_db)):
    Niveis = NiveisRepository.find_by_id(db, id)
    if not Niveis:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nivel nao encontrado"
        )
    return NiveisResponse.from_orm(Niveis)

@app.delete("/api/niveis/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id_Niveis(id: int, db: Session = Depends(get_db)):
    if not NiveisRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nivel nao encontrado"
        )
    NiveisRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/niveis/{id}", response_model=NiveisResponse)
def update(id: int, request: NiveisRequest, db: Session = Depends(get_db)):
    if not NiveisRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Nivel noa encontrado"
        )
    Niveis = NiveisRepository.save(db, Niveis(id=id, **request.dict()))
    return NiveisResponse.from_orm(Niveis)


@app.post("/api/niveis", response_model=NiveisResponse, status_code=status.HTTP_201_CREATED)
def create(request: NiveisRequest, db: Session = Depends(get_db)):
    Niveis = NiveisRepository.save(db, niveis(**request.dict()))
    return NiveisResponse.from_orm(Niveis)



@app.post("/api/niveis", response_model=NiveisResponse, status_code=status.HTTP_201_CREATED)
def create_Niveis(request: NiveisRequest, db: Session = Depends(get_db)):
    nivel = NiveisRepository.save(db, Niveis(**request.dict()))
    return NiveisResponse.from_orm(nivel)




# Código inicial do arquivo omitido para facilitação da leitura

@app.get("/api/Desenvolvedores", response_model=list[DesenvolvedoresResponse])
def find_all_Desenvolvedores(db: Session = Depends(get_db)):
    Desenvolvedores = DesenvolvedoresRepository.find_all(db)
    return [DesenvolvedoresResponse.from_orm(niveis) for niveis in Desenvolvedores]

# Código inicial do arquivo omitido para facilitação da leitura

@app.get("/api/Desenvolvedores/{id}", response_model=DesenvolvedoresResponse)
def find_by_id_Desenvolvedores(id: int, db: Session = Depends(get_db)):
    Desenvolvedores = DesenvolvedoresRepository.find_by_id(db, id)
    if not Desenvolvedores:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Desenvolvedor nao encontrado"
        )
    return DesenvolvedoresResponse.from_orm(Desenvolvedores)

@app.delete("/api/Desenvolvedores/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id_Desenvolvedores(id: int, db: Session = Depends(get_db)):
    if not DesenvolvedoresRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Desenvolvedor nao encontrado"
        )
    DesenvolvedoresRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/Desenvolvedores/{id}", response_model=DesenvolvedoresResponse)
def update(id: int, request: DesenvolvedoresRequest, db: Session = Depends(get_db)):
    if not DesenvolvedoresRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Desenvolvedor nao encontrado"
        )
    Desenvolvedores = DesenvolvedoresRepository.save(db, Desenvolvedores(id=id, **request.dict()))
    return DesenvolvedoresResponse.from_orm(Desenvolvedores)


@app.post("/api/Desenvolvedores", response_model=DesenvolvedoresResponse, status_code=status.HTTP_201_CREATED)
def create(request: DesenvolvedoresRequest, db: Session = Depends(get_db)):
    Desenvolvedores = DesenvolvedoresRepository.save(db, niveis(**request.dict()))
    return DesenvolvedoresResponse.from_orm(Desenvolvedores)