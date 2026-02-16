from .database import DBSession
async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
async with DBSession() as db:
    yield db
