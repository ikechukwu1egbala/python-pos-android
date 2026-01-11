from fastapi import FastAPI, HTTPException
from database import engine, SessionLocal
from models import Base
from crud import process_sale
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Python POS Backend")

class CartItem(BaseModel):
    product_id: int
    quantity: int

class SaleRequest(BaseModel):
    cart: list[CartItem]

@app.post("/checkout")
def checkout(data: SaleRequest):
    db = SessionLocal()
    try:
        sale = process_sale(
            db,
            cart=[item.dict() for item in data.cart],
        )
        return {"sale_id": sale.id, "total": sale.total}
    except ValueError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
      
