from fastapi import APIRouter, Body, Depends, HTTPException, status

from database.errors import EntityDoesNotExist
from database.sessions import get_repository
from repositories.currency import CurrencyRepository
from schemas.currency import Currency, CurrencyRead, CurrencyCreate

router = APIRouter(prefix='/currencies')


@router.get(
    '/',
    response_model=CurrencyRead,
    status_code=status.HTTP_200_OK,
    name='get_currencies',
)
async def get_currencies(
    repository: CurrencyRepository = Depends(get_repository(CurrencyRepository)),
) -> CurrencyRead:
    try:
        result = await repository.get(model=Currency)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Currencies not found'
        )
    return result


@router.post(
    '/',
    response_model=CurrencyRead,
    status_code=status.HTTP_201_CREATED,
    name='create_currencies',
)
async def create_currencies(
    model_create: CurrencyCreate = Body(...),
    repository: CurrencyRepository = Depends(get_repository(CurrencyRepository)),
) -> CurrencyRead:
    try:
        result = await repository.create(model=Currency, model_create=model_create)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f'Error: {e}'
        )
    return result
