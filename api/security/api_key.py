import os
from dotenv import load_dotenv
from fastapi import Security, Depends, HTTPException, Request
from fastapi.security import APIKeyHeader
from schemas.security import SecurityResult

load_dotenv()

SECURITY_API_KEY = os.getenv('SECURITY_API_KEY')
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

def verify_api_key(    
    api_key: str = Security(api_key_header)
) -> SecurityResult:
    if not SECURITY_API_KEY or api_key != SECURITY_API_KEY:
        return SecurityResult(
            authorized=False,
            status_code=401,
            detail="Unauthorized"
        )

    return SecurityResult(
        authorized=True,
        status_code=200,
        detail="Authorized"
    )
