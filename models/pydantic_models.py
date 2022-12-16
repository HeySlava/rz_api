from data.models import Method, Datamart, Param
from pydantic_sqlalchemy import sqlalchemy_to_pydantic


PydanticDatamart = sqlalchemy_to_pydantic(Datamart)
PydanticParam = sqlalchemy_to_pydantic(Param)
PydanticMethod = sqlalchemy_to_pydantic(Method)


class PydanticMethodWithParams(PydanticMethod):
    params: list[PydanticParam]


class PydanticDatamartsWithMethods(PydanticDatamart):
    methods: list[PydanticMethodWithParams]
