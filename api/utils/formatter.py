import httpx, time, os
from dotenv import load_dotenv
from fastapi import FastAPI, Request

load_dotenv()
API_URL = os.getenv("STREAMLIT_URL_API")
_HEADERS = ("authorization", "x-api-key", "x-request-id")
class FormatResponse:
    def __init__(self, app: FastAPI) -> None:
        self.app = app

    async def from_request(self, request: Request) -> dict[str, Any]:
        params = {k: v for k, v in request.query_params.items() if k != "need_format"}
        headers = {k: v for k, v in request.headers.items() if k in _HEADERS}
        return await self.response_complete(request.url.path, params=params, headers=headers, method=request.method)

    async def response_complete(self, path: str, *, params=None, headers=None, method: str = "GET") -> dict[str, Any]:
        print('====== IN FORMATTER =========')
        transport = httpx.ASGITransport(app=self.app, raise_app_exceptions=False)
        async with httpx.AsyncClient(transport=transport, base_url=API_URL) as client:
            start_time = time.perf_counter()
            try:
                print('in try')
                res = await client.request(method, path, params=params, headers=headers)
                print(res)
            except httpx.HTTPError as exc:
                ms = round((time.perf_counter() - start_time) * 1000, 2)
                return {"status_code":None, "ms":ms, "headers":{}, "body":None, "error":str(exc), "detail":str(exc)}
            ms = round((time.perf_counter() - start_time) * 1000, 2)
            print(res)
        try:
            body = res.json()
        except ValueError:
            body = res.text
        detail = str(body.get("detail", body)) if isinstance(body, dict) else str(body)
        return {"status_code":res.status_code, "ms":ms, "headers":dict(res.headers), "body":body, "detail":detail}