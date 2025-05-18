from sqlmodel import  create_engine, SQLModel

from models import Sales, Inventory,Products,Inventory_history


def create_db():
    engine = create_engine(str("postgresql+psycopg2://postgres:postgres@localhost:5432/ecommerceapi"))
    SQLModel.metadata.create_all(engine)


if __name__=="__main__":
    print("Creating Tables")
    create_db()
    print("Tables Created Successfully")
    