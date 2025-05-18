from sqlmodel import  create_engine, SQLModel

from models import Sales, Inventory,Products,Inventory_history


def drop_tables():
    engine = create_engine(str("postgresql+psycopg2://postgres:postgres@localhost:5432/ecommerceapi"))
    SQLModel.metadata.drop_all(engine)


if __name__=="__main__":
    print("dropping tables")
    drop_tables()
    print("tables probably dropped")