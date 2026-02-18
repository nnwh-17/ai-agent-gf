# imports
from typing import Annotated
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

# create model - definition of a user
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    password: str = Field(index=True)
    created_at: datetime = Field(default=datetime.now(), index=True)
    
# create engine - holds connections to the db
sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

connect_args = {'check_same_thread': False}
engine = create_engine(sqlite_url, connect_args=connect_args)

# create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
# create session
def get_session():
    with Session(engine) as session:
        yield session
        
SessionDep = Annotated[Session, Depends(get_session)]

# app
app = FastAPI()

# create db tables on startup
@app.on_event('startup')
def on_startup():
    create_db_and_tables()
    
# endpoints

# Health Check
@app.get("/")
async def root():
    return {"message": "Hello World"}

# create user
@app.post('/users')
def create_user(
    user: User, 
    session: SessionDep
) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# read user
@app.get('/users')
def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[User]:
    heroes = session.exec(select(User).offset(offset).limit(limit)).all()
    return heroes

@app.get('/users/{user_id}')
def read_user(
    user_id: int, 
    session: SessionDep
) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# delete user
@app.delete('/users/{user_id}')
def delete_user(
    user_id: int, 
    session: SessionDep
):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}