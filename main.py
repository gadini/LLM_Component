from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from src.router.completion import LLMRouter

app = FastAPI()

# Configuração do middleware CORS
origins = [
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Lista de origens permitidas
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],   # Permitir todos os cabeçalhos
)

app.include_router(LLMRouter)
