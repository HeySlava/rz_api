from data.models import Datamart, Method
from data.models import Param
from sqlalchemy.orm import Session


def get_methods(db: Session) -> list[Method]:
    return db.query(Method).all()


def get_datamarts(db: Session) -> list[Method]:
    return db.query(Datamart).all()
