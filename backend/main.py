from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models
import schemas

app = FastAPI()
# Criando as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Rotas dos níveis
@app.post("/niveis/", response_model=schemas.NivelOut)
def create_nivel(nivel: schemas.NivelCreate, db: Session = Depends(get_db)):
    db_nivel = models.Nivel(nivel=nivel.nivel)
    db.add(db_nivel)
    db.commit()
    db.refresh(db_nivel)
    return db_nivel

@app.get("/niveis/{nivel_id}", response_model=schemas.NivelOut)
def read_nivel(nivel_id: int, db: Session = Depends(get_db)):
    db_nivel = db.query(models.Nivel).filter(models.Nivel.id == nivel_id).first()
    if db_nivel is None:
        raise HTTPException(status_code=404, detail="Nível não encontrado")
    return db_nivel

@app.get("/niveis/", response_model=list[schemas.NivelOut])
def read_niveis(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    niveis = db.query(models.Nivel).offset(skip).limit(limit).all()
    return niveis

@app.put("/niveis/{nivel_id}", response_model=schemas.NivelOut)
def update_nivel(nivel_id: int, nivel: schemas.NivelUpdate, db: Session = Depends(get_db)):
    db_nivel = db.query(models.Nivel).filter(models.Nivel.id == nivel_id).first()
    if db_nivel is None:
        raise HTTPException(status_code=404, detail="Nível não encontrado")
    db_nivel.nivel = nivel.nivel
    db.commit()
    db.refresh(db_nivel)
    return db_nivel

@app.delete("/niveis/{nivel_id}")
def delete_nivel(nivel_id: int, db: Session = Depends(get_db)):
    db_nivel = db.query(models.Nivel).filter(models.Nivel.id == nivel_id).first()
    if db_nivel is None:
        raise HTTPException(status_code=404, detail="Nível não encontrado")
    db.delete(db_nivel)
    db.commit()
    return {"message": "Nível deletado com sucesso"}


# Rotas dos desenvolvedores
@app.post("/desenvolvedores", response_model=schemas.DesenvolvedorOut)
def create_desenvolvedor(desenvolvedor: schemas.DesenvolvedorCreate, db: Session = Depends(get_db)):
    db_nivel = db.query(models.Nivel).filter(models.Nivel.id == desenvolvedor.idNivel).first()
    if not db_nivel:
        raise HTTPException(status_code=404, detail="Nivel não encontrado")
    db_desenvolvedor = models.Desenvolvedor(nome=desenvolvedor.nome, idNivel=desenvolvedor.idNivel)
    db.add(db_desenvolvedor)
    db.commit()
    db.refresh(db_desenvolvedor)
    return db_desenvolvedor

@app.get("/desenvolvedores/{desenvolvedor_id}", response_model=schemas.DesenvolvedorOut)
def read_desenvolvedor(desenvolvedor_id: int, db: Session = Depends(get_db)):
    db_desenvolvedor = db.query(models.Desenvolvedor).filter(models.Desenvolvedor.id == desenvolvedor_id).first()
    if not db_desenvolvedor:
        raise HTTPException(status_code=404, detail="Desenvolvedor não encontrado")
    return db_desenvolvedor

@app.put("/desenvolvedores/{desenvolvedor_id}", response_model=schemas.DesenvolvedorOut)
def update_desenvolvedor(desenvolvedor_id: int, desenvolvedor: schemas.DesenvolvedorUpdate, db: Session = Depends(get_db)):
    db_desenvolvedor = db.query(models.Desenvolvedor).filter(models.Desenvolvedor.id == desenvolvedor_id).first()
    if not db_desenvolvedor:
        raise HTTPException(status_code=404, detail="Desenvolvedor não encontrado")
    if desenvolvedor.nome:
        db_desenvolvedor.nome = desenvolvedor.nome
    if desenvolvedor.idNivel:
        db_nivel = db.query(models.Nivel).filter(models.Nivel.id == desenvolvedor.idNivel).first()
        if not db_nivel:
            raise HTTPException(status_code=404, detail="Nivel não encontrado")
        db_desenvolvedor.idNivel = desenvolvedor.idNivel
    db.commit()
    db.refresh(db_desenvolvedor)
    return db_desenvolvedor

@app.delete("/desenvolvedores/{desenvolvedor_id}")
def delete_desenvolvedor(desenvolvedor_id: int, db: Session = Depends(get_db)):
    db_desenvolvedor = db.query(models.Desenvolvedor).filter(models.Desenvolvedor.id == desenvolvedor_id).first()
    if not db_desenvolvedor:
        raise HTTPException(status_code=404, detail="Desenvolvedor não encontrado")
    db.delete(db_desenvolvedor)
    db.commit()
    return {"mensagem": "Desenvolvedor deletado com sucesso"}