from fastapi import APIRouter, HTTPException
from uuid import UUID
from session_provider import current_session
from models import Products
from schemas import Product_Created,Product
from crud import register_product_dao,get_product_by_uuid

router = APIRouter(prefix="/products",tags=["Products"])

@router.get("/{product_uuid}", response_model=Products)
def read_product(session:current_session,product_uuid:UUID):
    try:
        product = get_product_by_uuid(session=session,product_uuid=product_uuid)
        if not product:
            raise HTTPException(status_code=404, detail="product does not exists")
        return product
    except:
        raise HTTPException(status_code=503, detail="request cannot be processed right now")


@router.post("/register-new-product", response_model=Product_Created)       
def register_product(session:current_session, product_input:Product):
    try:
        product = register_product_dao(session=session,new_product=product_input)
        if not product:
            raise HTTPException(status_code=404, detail="product can not be registered")
        return product
    except:
        raise HTTPException(status_code=503, detail="request cannot be processed right now")