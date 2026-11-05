from dataclasses import dataclass

@dataclass
class SecurityResult:
    authorized: bool
    status_code: int
    detail: str
