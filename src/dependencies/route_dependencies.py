def get_session():
    """FastAPI Dependency to inject  sqlalchemy session object"""
    from src.mappers.database import SessionLocal

    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
