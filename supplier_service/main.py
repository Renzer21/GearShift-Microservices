from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from bson import ObjectId

app = FastAPI(title="Supplier Service")

client = AsyncIOMotorClient("mongodb+srv://vihanga1:Srilanka1234@cluster0.vkq9t3u.mongodb.net/gearshop")
db = client.gearshift_suppliers

class Supplier(BaseModel):
    brand_name: str
    contact_email: str

@app.post("/suppliers/")
async def add_supplier(supplier: Supplier):
    new_sup = await db.suppliers.insert_one(supplier.dict())
    return {"message": "Supplier added", "id": str(new_sup.inserted_id)}

