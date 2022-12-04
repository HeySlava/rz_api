from typing import Iterable
import sqlalchemy as sa
from sqlalchemy import orm

from data.basemodel import Base

_factory = None


def global_init(conn_str: str, debug: bool = False):
    global _factory

    if _factory:
        return 

    if not conn_str or not conn_str.strip():
        raise Exception(f'Wrong {conn_str=!r}')


    engine = sa.create_engine(conn_str, echo=debug,
            connect_args={'check_same_thread':False})

    _factory  = orm.sessionmaker(engine)
    import data._all_models
    Base.metadata.create_all(engine)


def create_session() -> Iterable[orm.Session]:
    global _factory


    if not _factory:
        raise Exception('You have to run global_init() before')


    session: orm.Session = _factory()
    session.expire_on_commit = False

    try:
        yield session
    finally:
        session.close()
