

import datetime
from random import randint, random
from sqlmodel import Session, create_engine
from schemas import Product,Product_Created
from crud import register_product_dao,update_Inventory
from models import Inventory,Sales

engine = create_engine(str("postgresql+psycopg2://postgres:postgres@localhost:5432/ecommerceapi"))

sessionn= Session(engine) 

productsList = [
    Product(name="Air Conditioner", description="This is an Air Conditioner", cost=200, price=400, category="Appliances"),
    Product(name="Laptop", description="This is a powerful laptop", cost=700, price=1000, category="Electronics"),
    Product(name="Office Chair", description="Ergonomic office chair", cost=50, price=120, category="Furniture"),
    Product(name="Running Shoes", description="Comfortable running shoes", cost=30, price=80, category="Footwear"),
    Product(name="Blender", description="High-speed kitchen blender", cost=25, price=60, category="Kitchen"),
    Product(name="Smartphone", description="Latest model smartphone", cost=300, price=700, category="Electronics"),
    Product(name="T-shirt", description="Cotton round-neck t-shirt", cost=5, price=20, category="Clothing"),
    Product(name="Electric Kettle", description="1.5L stainless steel kettle", cost=15, price=40, category="Appliances"),
    Product(name="Mountain Bike", description="Off-road mountain bike", cost=250, price=600, category="Sports"),
    Product(name="Wrist Watch", description="Analog wrist watch with leather strap", cost=20, price=50, category="Accessories"),
    Product(name="Gaming Console", description="Next-gen gaming console with 4K support", cost=350, price=550, category="Electronics"),
    Product(name="Microwave Oven", description="800W compact microwave oven", cost=60, price=120, category="Appliances"),
    Product(name="Yoga Mat", description="Non-slip eco-friendly yoga mat", cost=10, price=30, category="Fitness"),
    Product(name="Bookshelf", description="5-tier wooden bookshelf", cost=40, price=100, category="Furniture"),
    Product(name="Leather Wallet", description="Men's genuine leather wallet", cost=8, price=25, category="Accessories"),
    Product(name="LED Desk Lamp", description="Dimmable LED desk lamp with USB port", cost=12, price=35, category="Lighting"),
    Product(name="Espresso Machine", description="Compact espresso coffee machine", cost=90, price=180, category="Kitchen"),
    Product(name="Winter Jacket", description="Insulated waterproof winter jacket", cost=60, price=150, category="Clothing"),
    Product(name="Bluetooth Speaker", description="Portable waterproof Bluetooth speaker", cost=25, price=60, category="Electronics"),
    Product(name="Tennis Racket", description="Lightweight graphite tennis racket", cost=35, price=90, category="Sports")
]


if __name__ == "__main__":

    sr_no_list = []
    for each in productsList:
        product = register_product_dao(session=sessionn,new_product=each)
        sr_no = product.product_srno
        sr_no_list.append(sr_no)
        update_Inventory(session=sessionn,product_srno=sr_no,change_amount=randint(10,100))


    # below code for genereting thousand sales for analytics purposes
    start_date = datetime.date(2023, 5, 18)
    end_date = datetime.date(2025, 5, 18)
    delta_days = (end_date - start_date).days

    # Generate 1000 Sales objects
    sales_data = [
        Sales(
            product_srno=randint(1, 20),
            no_of_items=randint(1, 10),
            order_date=start_date + datetime.timedelta(days=randint(0, delta_days))
        )
        for _ in range(1000)
    ]
    print(sales_data)

    for each in sales_data:
        sessionn.add(each)
    sessionn.commit()
    sessionn.close()


        



    