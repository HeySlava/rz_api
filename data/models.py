import sqlalchemy as sa
from sqlalchemy import orm
from data.basemodel import Base


class Datamart(Base):
    __tablename__ = 'datamarts'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    datamart: str = sa.Column(sa.String)
    methods = orm.relationship('Method', back_populates='datamart')


class Method(Base):
    __tablename__ = 'methods'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    method: str = sa.Column(sa.String)

    datamart_id = sa.Column(sa.Integer, sa.ForeignKey('datamarts.id'))
    datamart = orm.relationship('Datamart', back_populates='methods')
    params = orm.relationship('Param', back_populates='method')


class Param(Base):
    __tablename__ = 'params'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    param: str = sa.Column(sa.String)

    method_id: int = sa.Column(sa.Integer, sa.ForeignKey('methods.id'))
    method = orm.relationship('Method', back_populates='params')
