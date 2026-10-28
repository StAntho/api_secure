from pathlib import Path
from fastapi import HTTPException

class PublicDataService:
    GENERATED_DIR = Path("generations")

    def __init__(
        self
    ):
        self.GENERATED_DIR.mkdir(exist_ok=True)

    def public_info(self) -> dict:
        try:
            address = "122 rue de Paris, 75001 Paris"

            return {"address": address}
    
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))