
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..utils.schema import Request
from ..llm.call import LLM

llm = LLM()

LLMRouter = APIRouter(
    tags=["LLM Completion"],
    prefix="/llm-completion"
)

@LLMRouter.post("/llm-call")
async def call_llm(request: Request):
    response = llm.completion(content=request.content)
    return {"Response": response} 