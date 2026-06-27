from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.middleware import SlowAPIMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.exceptions import global_exception_handler
from app.core.rate_limiter import limiter
from app.database import Base, engine

import app.models
from app.routes import router

import os

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "..", "frontend")

# -----------------------------
# DB create tables
# -----------------------------
Base.metadata.create_all(bind=engine)

# -----------------------------
# App
# -----------------------------
app = FastAPI(
    title="MNS Service API",
    version="1.0"
)

# -----------------------------
# Static Frontend (IMPORTANT)
# -----------------------------
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

# -----------------------------
# Rate Limiting
# -----------------------------
app.state.limiter = limiter
app.add_exception_handler(Exception, global_exception_handler)
app.add_middleware(SlowAPIMiddleware)

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# API Routes (IMPORTANT: prefix)
# -----------------------------
app.include_router(router, prefix="/api")

# -----------------------------
# Health check (optional)
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}