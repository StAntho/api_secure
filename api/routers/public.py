from fastapi import APIRouter, Depends, Request
from services.public_service import PublicDataService
from utils.formatter import FormatResponse

router = APIRouter(prefix="/public_data", tags=["Public"])

@router.get("/info")
async def public_info(
    request: Request,
    need_format:bool = False,
    service: PublicDataService = Depends(PublicDataService)
):
    if need_format:
        return await FormatResponse(request.app).from_request(request)
    
    return service.public_info()