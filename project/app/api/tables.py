from fastapi import APIRouter


from app.api import crud

from app.models.pydantic import TablesPayloadSchema



router = APIRouter()

@router.post("/tables/create_new/")
async def create_table(payload: TablesPayloadSchema):
    print(payload)
    table_id = await crud.post_table(payload)
    response_object = {"id":table_id, "name":payload.name}
    return response_object
