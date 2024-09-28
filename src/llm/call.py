from .llm_wrapper import LLMWrapper
from ..prompt.prompt_builder import prompt

class LLM(LLMWrapper):
    def __init__(self) -> None:
        super().__init__()

    def completion(self, content: str) -> str:
        message = prompt.build(user_input=content)
        llm =  self.get_llm()
        response = llm.invoke(input=message)
        return response.content
