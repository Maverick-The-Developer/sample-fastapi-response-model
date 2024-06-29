from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import user_router


@asynccontextmanager
async def lifeSpan(app: FastAPI):
    print("#" * 20, " Starting Up Server")
    print("=" * 25, " Try Creating tables")
    Base.metadata.create_all(bind=engine)
    yield
    print("#" * 20, " Shutting Down Server")
    if engine:
        print("=" * 25, " Release DB connection")
        engine.dispose()


app = FastAPI(lifespan=lifeSpan)

# set cors policy
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(user_router, prefix="/user")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
