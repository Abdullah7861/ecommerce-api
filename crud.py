import datetime

from sqlmodel import UUID, Session, create_engine, func, select
from models import Products,Inventory,Sales
from schemas import Product,Product_Created,Inventory_Update,analytics_request_object_timewise,sales_analytics_object_timewise,analytics_response_object_timewise

engine = create_engine(str("postgresql+psycopg2://postgres:postgres@localhost:5432/ecommerceapi"))

sessionn= Session(engine) 



def register_product_dao(*, session: Session,new_product: Product) -> Product_Created:
   """
   inserting a new product into products table and inserting an
   inventory with 0 items in the inventory table

   """

   db_product_object = Products(
      name=new_product.name,
      description=new_product.description,
      cost=new_product.cost,
      price=new_product.price,
      category=new_product.category
   )

   session.add(db_product_object)
   session.commit()
   session.refresh(db_product_object)

   Inventory_object = Inventory(
      product_srno=db_product_object.product_srno,
      amount_available=0
   )

   session.add(Inventory_object)
   session.commit()
   session.refresh(Inventory_object)

   return Product_Created(
      product_id=db_product_object.product_id,
      product_srno=db_product_object.product_srno,
      name=db_product_object.name
      )

def get_product_by_uuid(*,session:Session,product_uuid:UUID):
   statement = select(Products).where(Products.product_id==product_uuid)
   results = session.exec(statement)
   product = results.one()

   return product


def get_inventory_by_srno(*,session:Session,product_srno:int):
   statement = select(Inventory).where(Inventory.product_srno==product_srno)
   results = session.exec(statement)
   product = results.one()
   
   return product


def get_sale_by_order_srno(*,session:Session,order_srno:int):
   statement = select(Sales).where(Sales.order_srno==order_srno)
   results = session.exec(statement)
   sale = results.one()
   
   return sale


def update_Inventory(*, session: Session,product_srno: int,change_amount:int):
   statement = select(Inventory).where(Inventory.product_srno==product_srno)
   results = session.exec(statement)
   Inventory_row = results.one()

   inventory_amount = Inventory_row.amount_available + change_amount

   Inventory_row.amount_available = inventory_amount

   session.add(Inventory_row)
   session.commit()
   session.refresh(Inventory_row)

   return Inventory_row


def sell_product(*, session:Session, product_srno : int, no_of_items:int):
   sold_product = Sales(
      product_srno=product_srno,
      no_of_items = no_of_items
   )


   session.add(sold_product)
   session.commit()
   session.refresh(sold_product)

   update_Inventory(session=session,product_srno=product_srno,change_amount=(-1*no_of_items))

   return sold_product

def get_daily_sales_analytics(*,session:Session,request_obj:analytics_request_object_timewise):
    statement = (
        select(
            func.sum(Products.cost).label("total_cost"),
            func.sum(Products.price).label("total_price"),
            func.sum(Sales.no_of_items).label("total_items"),
            Sales.order_date
        ).join(Products, Sales.product_srno == Products.product_srno)
        .where(Sales.order_date.between(request_obj.from_date, request_obj.to_date))
        .group_by(Sales.order_date)
        .order_by(Sales.order_date.asc())
        .limit(request_obj.no_of_records)
    )



    results = session.exec(statement).all()

    daily_results_list = []

    for total_cost, total_price, total_items, order_date in results:
       revenue = total_price - total_cost
       daily_results_list.append(
          sales_analytics_object_timewise(
             cost=total_cost,
             price=total_price,
             revenue=revenue,
             no_of_products=total_items,
             date_from=order_date,
             date_to=order_date
             )
       )

    response_object = analytics_response_object_timewise(
       no_of_records=len(daily_results_list),
       sales=daily_results_list
    )

    return response_object

if __name__== "__main__":
   request = analytics_request_object_timewise(
    granularity="daily",
    from_date=datetime.date(2024, 6, 1),
    to_date=datetime.date(2024, 6, 30),
    no_of_records=100,
    category=""
   )
   print(get_daily_sales_analytics(session=sessionn,request_obj=request))
   
 