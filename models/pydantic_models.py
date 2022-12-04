from data.models import Method, Datamart, Param
from pydantic_sqlalchemy import sqlalchemy_to_pydantic


PydanticParam = sqlalchemy_to_pydantic(Param)

PydanticMethod = sqlalchemy_to_pydantic(Method)

class PydanticMethodWithParams(PydanticMethod):
    params: list[PydanticParam]



PydanticDatamart = sqlalchemy_to_pydantic(Datamart)
