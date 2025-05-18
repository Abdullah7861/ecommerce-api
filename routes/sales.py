from fastapi import APIRouter, HTTPException
from session_provider import current_session
from crud import get_sale_by_order_srno,sell_product
from models import Sales
router = APIRouter(prefix="/sales", tags=["sales"])


@router.get("/{order_id}", response_model=Sales)
def read_sales(session:current_session,order_id:int):
    
    sale = get_sale_by_order_srno(session=session,order_srno=order_id)

    if not sale:
        raise HTTPException(status_code=404, detail="product does not exists")
    return sale

@router.post("/sell", response_model=Sales)
def sell(session:current_session,product_srno:int,no_of_items:int):
    
    sold = sell_product(session=session,product_srno=product_srno,no_of_items=no_of_items)
    if not sold:
        raise HTTPException(status_code=404, detail="product does not exists")
    return sold