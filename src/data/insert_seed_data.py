def insert_initial_data():
    from src.dependencies.route_dependencies import get_session
    from src.data.seed_data import users, items
    from sqlalchemy.orm import Session

    session: Session = next(get_session())
    session.add_all(users)
    session.commit()
    session.add_all(items)
    session.commit()


if __name__ == "__main__":
    print("\033[32mINFO\033[0m:     Inserting seed data to database.")
    insert_initial_data()
