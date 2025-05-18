from fastapi import APIRouter,FastAPI
from routes import inventory,product,sales,analytics



api_router = APIRouter()
api_router.include_router(inventory.router)
api_router.include_router(product.router)
api_router.include_router(sales.router)
api_router.include_router(analytics.router)
app = FastAPI(
    title="Test Project",
    openapi_url="/api/v1/openapi.json"
)


app.include_router(api_router, prefix="/api/v1")

