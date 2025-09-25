from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from logger import GLOBAL_LOGGER as log
from fastapi.responses import JSONResponse

app = FastAPI(title="Intelli agent Portal API", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello():
    log.info("Serving UI homepage.")
    return JSONResponse(status_code=200,content={'message':'Started successfully'})

@app.get("/health")
def health() -> Dict[str, str]:
    log.info("Health check passed.")
    return {"status": "ok", "service": "document-portal"}