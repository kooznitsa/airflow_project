from sqlalchemy import select
from sqlmodel.ext.asyncio.session import AsyncSession


class BaseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _add_to_db(self, new_item):
        self.session.add(new_item)
        await self.session.commit()
        await self.session.refresh(new_item)

    async def create(self, model, model_create):
        result = model.from_orm(model_create)
        await self._add_to_db(result)
        return result

    async def get(self, model):
        query = select(model).order_by(model.id.desc())
        result = await self.session.scalars(query)
        return result.first()
