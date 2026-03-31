from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from bson import ObjectId

app = FastAPI(title="Customer Service")

client = AsyncIOMotorClient("mongodb+srv://vihanga1:Srilanka1234@cluster0.vkq9t3u.mongodb.net/gearshop")
db = client.gearshift_customers

class Customer(BaseModel):
    name: str
    phone: str
    shop_name: str

@app.post("/customers/")
async def add_customer(customer: Customer):
    new_cust = await db.customers.insert_one(customer.dict())
    return {"message": "Customer added", "id": str(new_cust.inserted_id)}

@app.get("/customers/")
async def get_customers():
    customers = await db.customers.find().to_list(100)
    for c in customers:
        c["_id"] = str(c["_id"])
    return customers

@app.get("/customers/{id}")
async def get_customer(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    customer = await db.customers.find_one({"_id": ObjectId(id)})
    if customer:
        customer["_id"] = str(customer["_id"])
        return customer
    raise HTTPException(status_code=404, detail="Customer not found")

@app.put("/customers/{id}")
async def update_customer(id: str, customer: Customer):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await db.customers.update_one({"_id": ObjectId(id)}, {"$set": customer.dict()})
    if result.modified_count == 1:
        return {"message": "Customer updated"}
    raise HTTPException(status_code=404, detail="Customer not found")

@app.delete("/customers/{id}")
async def delete_customer(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await db.customers.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Customer deleted"}
    raise HTTPException(status_code=404, detail="Customer not found")