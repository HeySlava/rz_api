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
