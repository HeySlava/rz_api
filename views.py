import schemes
from fastapi import APIRouter



router = APIRouter()



@router.get('/getMethods', response_model=list[schemes.MethodModel])
async def get_methods():
    return [
            {
                'id': 1,
                'method': 'method1',
                'params': [
                    {'id': 1, 'param': 'param1'},
                    {'id': 2, 'param': 'param2'}
                ]
            },
            {
                'id': 2,
                'method': 'method2',
                'params': [
                    {'id': 1, 'param': 'param1'},
                    {'id': 2, 'param': 'param2'}
                ]
            }
        ]



@router.get('/getDatamarts', response_model=list[schemes.DatamartModel])
async def get_datamarts():
    return [
            {
                'id': 1,
                'datamart': 'datamart1'
            },
            {
                'id': 2,
                'datamart': 'datamart1'
            }
        ]
