from fastapi import APIRouter, Depends, Request
from services.private_service import PrivateDataService
from utils.formatter import FormatResponse
from security.api_key import verify_api_key
from schemas.security import SecurityResult

router = APIRouter(prefix="/private_data", tags=["Private"])

@router.get("/info")
async def private_info(
    request: Request,
    need_format: bool = False,
    security: SecurityResult = Depends(verify_api_key),
    service: PrivateDataService = Depends(PrivateDataService)
):
    formatter = FormatResponse(request.app)

    if not security.authorized:

        if need_format:
            return await formatter.format_security_error(security)

        from fastapi.responses import JSONResponse

        return JSONResponse(
            status_code=security.status_code,
            content={"detail": security.detail}
        )

    if need_format:
        return await formatter.from_request(request)

    return service.public_api_info()