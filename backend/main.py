import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import router as ws_router, _warmup_models
from backend.api.classroom_routes import router as classroom_router
from backend.api.stats_routes import router as stats_router
from backend.api.chat_routes import router as chat_router
from backend.api.person_routes import router as person_router
from backend.api.rag_routes import router as rag_router
from backend.core.database import init_db
from backend.models import tables  # noqa: F401 — 确保 Base 能发现所有表


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, _warmup_models)
    yield


app = FastAPI(title="ClassVision API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ws_router)
app.include_router(classroom_router)
app.include_router(stats_router)
app.include_router(chat_router)
app.include_router(person_router)
app.include_router(rag_router)


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "service": "ClassVision"}
