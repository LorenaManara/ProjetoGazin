from sqlalchemy.orm import Session

from models import Niveis, Desenvolvedores

class NiveisRepository:
    @staticmethod
    def find_all_Niveis(db: Session) -> list[Niveis]:
        return db.query(Niveis).all()

    @staticmethod
    def save_Niveis(db: Session, niveis: Niveis) -> Niveis:
        if niveis.id:
            db.merge(niveis)
        else:
            db.add(niveis)
        db.commit()
        return niveis

    @staticmethod
    def find_by_id_Niveis(db: Session, id: int) -> Niveis:
        return db.query(Niveis).filter(Niveis.id == id).first()

    @staticmethod
    def exists_by_id_Niveis(db: Session, id: int) -> bool:
        return db.query(Niveis).filter(Niveis.id == id).first() is not None

    @staticmethod
    def delete_by_id_Niveis(db: Session, id: int) -> None:
        niveis = db.query(Niveis).filter(Niveis.id == id).first()
        if niveis is not None:
            db.delete(niveis)
            db.commit()



class DesenvolvedoresRepository:
    @staticmethod
    def find_all_Desenvolvedores(db: Session) -> list[Desenvolvedores]:
        return db.query(Desenvolvedores).all()

    @staticmethod
    def save_Desenvolvedores(db: Session, desenvolvedores: Desenvolvedores) -> Desenvolvedores:
        if desenvolvedores.id:
            db.merge(desenvolvedores)
        else:
            db.add(desenvolvedores)
        db.commit()
        return desenvolvedores

    @staticmethod
    def find_by_id_Desenvolvedores(db: Session, id: int) -> Desenvolvedores:
        return db.query(Desenvolvedores).filter(Desenvolvedores.id == id).first()

    @staticmethod
    def exists_by_id_Desenvolvedores(db: Session, id: int) -> bool:
        return db.query(Desenvolvedores).filter(Desenvolvedores.id == id).first() is not None

    @staticmethod
    def delete_by_id_Desenvolvedores(db: Session, id: int) -> None:
        desenvolvedores = db.query(Desenvolvedores).filter(Desenvolvedores.id == id).first()
        if desenvolvedores is not None:
            db.delete(desenvolvedores)
            db.commit()
