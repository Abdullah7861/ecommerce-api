# ecommerce-api
This Simple Project is Created as Take Home Task for Forsit Backend Developer role

Setup Instruction and Dependencies:

    The project is developed without virtual environment, so to run the project following dependcies are required on the machine
    running the project.

        1. fastapi[standard]
        2. pydantic
        3. psycopg2
        4. sqlmodel

    After Installation of the above written module through pip or any other package manager.
    The app can be started from terminal by the command: fastapi dev main.py





Below is the description of API Endpoints:

#############  Products #################

1.  api/v1/products/{product_uuid}
   --> Description: API Endpoint to get the complete description of a Product from its unique uuid

2.  api/v1/products/register-new-product
   --> Description : Endpoint to register a new product by providing its information.

#############   Inventory ################

1. api/v1/inventory/{id}
   --> Description: Endpoint to get the information of inventory of a product from its serial number

2. api/v1/inventory/update-inventory
   --> Decription: Endpoint to update the inventory of a product by providing the required and relevant information

#############    Sales   #################

1. api/v1/sales/{order_id}
   --> Description: Endpoint to get the sales data against the order id

2. api/v1/sales/sell
   --> Description: Endpoint to sale a product, i.e. to provide information of sales entry 

#############   Analytics ################

1. api/v1/analytics/timewise/
   --> Description: Endpoint to get the sales data , i.e. cost, price, revenue for a given timeperiod and given granularity
                    such as daily, weekly , monthly or annualy



