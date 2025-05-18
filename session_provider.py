from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import Session, create_engine

engine = create_engine(str("postgresql+psycopg2://postgres:postgres@localhost:5432/ecommerceapi"))

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


current_session = Annotated[Session, Depends(get_db)]