import uvicorn
from src.api.routers.user import user_router
from src.domain.orm.user import start_mappers
from src.mappers.metadata import create_tables
from fastapi import FastAPI


app = FastAPI()
app.include_router(user_router)


@app.on_event("startup")
def on_startup():
    print("\033[32mINFO\033[0m:     Starting up... creating tables if not exist")
    create_tables()
    print("\033[32mINFO\033[0m:     Mapping tables in an classical mapping way")
    start_mappers()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
