from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models.pydantic.livestream import LivestreamCreate, LivestreamOut
from services.livestream import create_livestream, get_livestream_by_id
from database.session import get_async_session

router = APIRouter()

@router.post("/", response_model=LivestreamOut)
async def create_new_livestream(
    data: LivestreamCreate,
    session: AsyncSession = Depends(get_async_session)
):
    return await create_livestream(data, session)


@router.get("/{livestream_id}", response_model=LivestreamOut)
async def get_livestream(
    livestream_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    result = await get_livestream_by_id(livestream_id, session)
    if not result:
        raise HTTPException(status_code=404, detail="Livestream not found")
    return result
