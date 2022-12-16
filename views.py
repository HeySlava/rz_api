from fastapi import APIRouter, Depends

import services
from models import schemes
from data.db_session import create_session

from models.pydantic_models import PydanticDatamart, PydanticMethodWithParams


router = APIRouter()


@router.get('/getMethods', response_model=list[schemes.MethodModel])
async def get_methods(db = Depends(create_session)):
    methods = services.get_methods(db)
    return [PydanticMethodWithParams.from_orm(m).dict() for m in methods]


@router.get('/getDatamarts', response_model=list[schemes.DatamartModel])
async def get_datamarts(db = Depends(create_session)):
    datamarts = services.get_datamarts(db)
    return  [PydanticDatamart.from_orm(d).dict() for d in datamarts]


@router.post('/dummy')
async def get_dummy(dummy: schemes.DummyModel):
    import requests
    return requests.post(url=dummy.url, headers=dummy.headers,
                         json=dummy.body.dict()).json()
