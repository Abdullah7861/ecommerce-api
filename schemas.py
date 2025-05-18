

# object to receive via api for product registration
import datetime
from typing import List
from uuid import UUID
from sqlmodel import  SQLModel
from enum import Enum

class Granularity(str, Enum):
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    yearly = "yearly"

class Product(SQLModel):
    name:str
    description:str
    cost:int
    price:int
    category:str


#object to return when a product is registered
class Product_Created(SQLModel):
    product_id : UUID
    product_srno: int
    name:str

#object to receive for update-inventory api
class Inventory_Update(SQLModel):
    product_srno:int
    change_amount:int


#object to receive requeset for analytics
class analytics_request_object_timewise(SQLModel):
    granularity : Granularity 
    from_date : datetime.date
    to_date : datetime.date
    no_of_records: int
    category:str | None


class sales_analytics_object_timewise(SQLModel):
    cost:int
    price:int
    revenue:int
    no_of_products:int
    date_from:datetime.date | None
    date_to:datetime.date | None


class analytics_response_object_timewise(SQLModel):
    no_of_records:int
    sales:List[sales_analytics_object_timewise]