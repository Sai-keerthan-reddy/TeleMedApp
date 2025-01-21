from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost:5432/TeleMedDb"

engine =create_async_engine(DATABASE_URL,echo= True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_ = AsyncSession)

#function to create tables
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



app= FastAPI()

@app.on_event("startup")
async def startup_event():
    await create_tables()


@app.get("/")
def home():
    return {"Hello":"world"}



