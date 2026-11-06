from fastapi import APIRouter, Depends, Request
from services.private_service import PrivateDataService
from utils.formatter import FormatResponse
from security.api_key import verify_api_key
from schemas.security import SecurityResult

router = APIRouter(prefix="/private_data", tags=["Private"])


@router.get("/info")
async def private_info(
    request: Request,
    need_format:bool = False,
    security: SecurityResult = Depends(verify_api_key),
    service: PrivateDataService = Depends(PrivateDataService)
):
    if not security.authorized:
        return await FormatResponse(request.app).format_security_error(security)

    if need_format:
        return await FormatResponse(request.app).from_request(request)

    return service.public_api_info()

