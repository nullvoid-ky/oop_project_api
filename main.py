from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .dependencies import create_token, verify_token
from .routers import auth


app = FastAPI(dependencies=[Depends(verify_token)])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    auth.router,
    prefix="/api",
    tags=["auth"]
)

@app.get("/")
async def read_root():
  return {"message": "This is API for Athletix website."}