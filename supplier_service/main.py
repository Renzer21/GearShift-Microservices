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

@app.get("/suppliers/")
async def get_suppliers():
    suppliers = await db.suppliers.find().to_list(100)
    for s in suppliers:
        s["_id"] = str(s["_id"])
    return suppliers

@app.get("/suppliers/{id}")
async def get_supplier(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    supplier = await db.suppliers.find_one({"_id": ObjectId(id)})
    if supplier:
        supplier["_id"] = str(supplier["_id"])
        return supplier
    raise HTTPException(status_code=404, detail="Supplier not found")

@app.put("/suppliers/{id}")
async def update_supplier(id: str, supplier: Supplier):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await db.suppliers.update_one({"_id": ObjectId(id)}, {"$set": supplier.dict()})
    if result.modified_count == 1:
        return {"message": "Supplier updated"}
    raise HTTPException(status_code=404, detail="Supplier not found")

@app.delete("/suppliers/{id}")
async def delete_supplier(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID")
    result = await db.suppliers.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Supplier deleted"}
    raise HTTPException(status_code=404, detail="Supplier not found")