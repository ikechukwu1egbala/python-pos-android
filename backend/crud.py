from sqlalchemy.orm import Session
from models import Product, Sale, SaleItem

def process_sale(db: Session, cart: list[dict]):
    total = 0.0
    sale_items = []

    for item in cart:
        product = db.query(Product).filter(Product.id == item["product_id"]).first()
        if not product:
            raise ValueError("Product not found")

        if product.stock < item["quantity"]:
            raise ValueError(f"Insufficient stock for {product.name}")

        product.stock -= item["quantity"]
        total += product.price * item["quantity"]

        sale_items.append(
            SaleItem(
                product_id=product.id,
                quantity=item["quantity"],
                price=product.price,
            )
        )

    sale = Sale(total=total)
    db.add(sale)
    db.flush()

    for si in sale_items:
        si.sale_id = sale.id
        db.add(si)

    db.commit()
    return sale
