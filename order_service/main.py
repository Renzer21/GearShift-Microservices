from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from bson import ObjectId

app = FastAPI(title="Order Service")

client = AsyncIOMotorClient("mongodb+srv://vihanga1:Srilanka1234@cluster0.vkq9t3u.mongodb.net/gearshop")
db = client.gearshift_orders

class Order(BaseModel):
    customer_name: str
    part_name: str
    quantity: int

@app.post("/orders/")
async def create_order(order: Order):
    new_order = await db.orders.insert_one(order.dict())
    return {"message": "Order placed", "id": str(new_order.inserted_id)}

@app.get("/orders/")
async def get_orders():
    orders = await db.orders.find().to_list(100)
    for o in orders:
        o["_id"] = str(o["_id"])
    return orders

@app.get("/orders/{id}")
async def get_order(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    order = await db.orders.find_one({"_id": ObjectId(id)})
    if order:
        order["_id"] = str(order["_id"])
        return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.put("/orders/{id}")
async def update_order(id: str, order: Order):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await db.orders.update_one({"_id": ObjectId(id)}, {"$set": order.dict()})
    if result.modified_count == 1:
        return {"message": "Order updated"}
    raise HTTPException(status_code=404, detail="Order not found")

@app.delete("/orders/{id}")
async def delete_order(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await db.orders.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Order deleted"}
    raise HTTPException(status_code=404, detail="Order not found")