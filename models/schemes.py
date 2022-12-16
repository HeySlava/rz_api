from pydantic import BaseModel


class ParamsModel(BaseModel):
    id: int
    param: str


class MethodModel(BaseModel):
    id: int
    method: str
    params: list[ParamsModel]
    

class DatamartModel(BaseModel):
    id: int
    datamart: str

class SQL(BaseModel):
    sql: str

class SQLbody(BaseModel):
    sql: SQL

class DummyModel(BaseModel):
    url: str
    body: SQLbody
    headers: dict
