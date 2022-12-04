import sqlalchemy as sa
from sqlalchemy import orm
from data.basemodel import Base


class Method(Base):
    __tablename__ = 'methods'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    method: str = sa.Column(sa.String)

    params = orm.relationship('Param', back_populates='method')


class Datamart(Base):
    __tablename__ = 'datamarts'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    datamart: str = sa.Column(sa.String)


class Param(Base):
    __tablename__ = 'params'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    param: str = sa.Column(sa.String)

    method_id = sa.Column(sa.Integer, sa.ForeignKey('methods.id'))
    method = orm.relationship('Method', back_populates='params')
