from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi.middleware import SlowAPIMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.exceptions import global_exception_handler
from app.core.rate_limiter import limiter
from app.database import Base, engine

import app.models
from app.routes import router   # your single routes file

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MNS Service API",
    version="1.0"
)
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

# Rate limiter setup
app.state.limiter = limiter
app.add_exception_handler(Exception, global_exception_handler)
app.add_middleware(SlowAPIMiddleware)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(router)


@app.get("/")
def home():
    return {"message": "MNS Backend Running"}