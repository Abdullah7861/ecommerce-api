import datetime
import uuid
from sqlmodel import Field, SQLModel
from uuid import UUID

class Products(SQLModel, table=True):
    product_srno:int | None = Field(default=None ,primary_key=True)
    product_id: UUID = Field(default_factory=uuid.uuid4, unique=True)
    name: str
    description: str
    cost: int 
    price: int 
    category: str

class Inventory(SQLModel, table=True):
    product_srno:int  = Field(foreign_key="products.product_srno", primary_key=True)
    amount_available:int
    last_updated_date:datetime.date = Field(default_factory=datetime.datetime.now(datetime.UTC).date, nullable=False)


class Inventory_history(SQLModel, table=True):
    product_srno:int  = Field(foreign_key="products.product_srno", primary_key=True)
    amount_available:int
    change_date:datetime.date = Field(default_factory=datetime.datetime.now(datetime.UTC).date, nullable=False)
    change_amount:int


class Sales(SQLModel, table=True):
    order_srno:int | None = Field(default=None ,primary_key=True)
    product_srno:int  = Field(foreign_key="products.product_srno", nullable=False)
    no_of_items:int
    order_date: datetime.date = Field(default_factory=datetime.datetime.now(datetime.UTC).date, nullable=False)


