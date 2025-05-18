
from fastapi import APIRouter, HTTPException
from session_provider import current_session
from models import Inventory
from schemas import Inventory_Update
from crud import update_Inventory,get_inventory_by_srno


router = APIRouter(prefix="/inventory",tags=["inventory"])


@router.get("/{id}", response_model=Inventory)
def read_inventory(session: current_session, id:int):
    """
    Get Inventory by product srno.
    """
    Inventory = get_inventory_by_srno(session=session,product_srno=id)
    if not Inventory:
        raise HTTPException(status_code=404, detail="Item not found")
    return Inventory



@router.post("/update-inventory", response_model=Inventory)
def create_inventory_item(session: current_session,new_inventory:Inventory_Update):


    updated_Inventory = update_Inventory(session=session, product_srno=new_inventory.product_srno, change_amount= new_inventory.change_amount)

    if not updated_Inventory:
        raise HTTPException(status_code=404, detail="Inventory can not be updated at this momment")
    
    return updated_Inventory