from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
from database import session_local, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Yoloco FastAPI")


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post('/add_user/{username}', tags=['Instagram'])
async def add_user_info(username: str, amount_of_media: int = 0, db: Session = Depends(get_db)) -> str:
    return crud.add_user_and_media_by_username(username, amount_of_media, db)


@app.get('/get_user/{username}', tags=['Instagram'], description='Returns a list with user data and all user posts')
async def get_user_info(username: str, db: Session = Depends(get_db)):
    db_info = crud.get_user_and_media_by_username(username, db)
    if db_info is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_info
