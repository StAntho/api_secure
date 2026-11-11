from fastapi import HTTPException
from utils.security import SecurityService

class PrivateDataService:
    def __init__(self):
        self.security = SecurityService()

    def public_api_info(self):
        return {
            "message": "Private API information",
            "access": "api users only"
        }


    def get_info(self, security_result):
        if not self.security.check(security_result):
            return self.security.format_result(security_result)

        return self.public_api_info()