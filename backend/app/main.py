from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.database import Base, engine
import app.models
from app.routes import router

import os

# ----------------------------
# DB init
# ----------------------------
Base.metadata.create_all(bind=engine)

# ----------------------------
# FastAPI app
# ----------------------------
app = FastAPI(
    title="MNS Service API",
    version="1.0"
)

# ----------------------------
# CORS
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Routes (API first)
# ----------------------------
app.include_router(router, prefix="/api")

# ----------------------------
# FRONTEND PATH FIX (IMPORTANT)
# ----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Docker-safe frontend path (IMPORTANT FIX)
FRONTEND_DIR = os.path.abspath(
    os.path.join(BASE_DIR, "..", "..", "frontend")
)

# Check if frontend exists (debug safety)
if os.path.exists(FRONTEND_DIR):
    app.mount(
        "/",
        StaticFiles(directory=FRONTEND_DIR, html=True),
        name="frontend"
    )
else:
    print("⚠️ Frontend folder not found at:", FRONTEND_DIR)


# ----------------------------
# Health check (API)
# ----------------------------
@app.get("/api/health")
def health():
    return {"status": "ok"}