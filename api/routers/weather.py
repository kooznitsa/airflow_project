from fastapi import APIRouter, Body, Depends, HTTPException, status

from database.errors import EntityDoesNotExist
from database.sessions import get_repository
from repositories.weather import WeatherRepository
from schemas.weather import Weather, WeatherCreate, WeatherRead

router = APIRouter(prefix='/weather')


@router.get(
    '/',
    response_model=WeatherRead,
    status_code=status.HTTP_200_OK,
    name='get_weather',
)
async def get_weather(
    repository: WeatherRepository = Depends(get_repository(WeatherRepository)),
) -> WeatherRead:
    try:
        result = await repository.get(model=Weather)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Weather not found'
        )
    return result


@router.post(
    '/',
    response_model=WeatherRead,
    status_code=status.HTTP_201_CREATED,
    name='create_weather',
)
async def create_weather(
    model_create: WeatherCreate = Body(...),
    repository: WeatherRepository = Depends(get_repository(WeatherRepository)),
) -> WeatherRead:
    try:
        result = await repository.create(model=Weather, model_create=model_create)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f'Error: {e}'
        )
    return result
