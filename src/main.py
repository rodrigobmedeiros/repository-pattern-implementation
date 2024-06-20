import uvicorn
from sqlalchemy.exc import IntegrityError
from src.api.routers.user import user_router
from src.data.insert_seed_data import insert_initial_data
from src.domain.orm.user import start_mappers
from src.mappers.base import create_tables
from fastapi import FastAPI


app = FastAPI()
app.include_router(user_router)


@app.on_event("startup")
def on_startup():
    print("\033[32mINFO\033[0m:     Starting up... creating tables if not exist")
    create_tables()
    print("\033[32mINFO\033[0m:     Mapping tables in an classical mapping way")
    start_mappers()
    print("\033[32mINFO\033[0m:     Inserting seed data to database.")
    try:
        insert_initial_data()
        print("\033[32mINFO\033[0m:     Data inserted.")
    except IntegrityError:
        print("\033[32mINFO\033[0m:     Data already inserted before.")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
