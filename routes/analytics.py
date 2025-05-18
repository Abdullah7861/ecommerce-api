from fastapi import APIRouter, HTTPException
from session_provider import current_session
from schemas import analytics_request_object_timewise,sales_analytics_object_timewise,analytics_response_object_timewise
from crud import get_daily_sales_analytics

router = APIRouter(prefix="/analytics",tags=["analytics"])

@router.post("/timewise/",response_model=analytics_response_object_timewise)
def get_analytics(Session: current_session, request_object:analytics_request_object_timewise):
    """
    Get analytics

    """

    result = None
    if(request_object.granularity == "daily"):
        result = get_daily_sales_analytics(session=Session,request_obj=request_object)
    print(result)
    return result



