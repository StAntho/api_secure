from fastapi import APIRouter, Depends
from services.public_service import PublicDataService

router = APIRouter(prefix="/public_data", tags=["Public"])

@router.get("/info")
def public_info(
    service: PublicDataService = Depends(PublicDataService)
):
    return service.public_info()