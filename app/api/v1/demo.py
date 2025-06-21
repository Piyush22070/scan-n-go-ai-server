from fastapi import APIRouter

router = APIRouter()

@router.get("/hello-synapse")
async def hello_synapse():
    return {"message": "Hello, Synapse!"}
