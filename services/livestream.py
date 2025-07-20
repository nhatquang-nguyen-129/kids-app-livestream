from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.orm.livestream import Livestream
from models.pydantic.livestream import LivestreamCreate
from sqlalchemy import insert
import json


async def create_livestream(data: LivestreamCreate, session: AsyncSession):
    new_livestream = Livestream(
        title=data.title,
        description=data.description,
        scheduled_time=data.scheduled_time,
        product_ids=data.product_ids,
        created_by=data.created_by,
    )
    session.add(new_livestream)
    await session.commit()
    await session.refresh(new_livestream)
    return new_livestream


async def get_livestream_by_id(livestream_id: int, session: AsyncSession):
    result = await session.execute(
        select(Livestream).where(Livestream.id == livestream_id)
    )
    return result.scalar_one_or_none()
